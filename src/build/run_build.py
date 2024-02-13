from flask import abort, request, Response
import datetime
import requests
import os, sys
from git.exc import GitCommandError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from payload import Payload
from utils.utils import verify_webhook_signature, _clone_repo, _remove_repo
from utils.run_tests import run_tests
from utils.run_syntax import syntax_checker


def set_status(commit_sha, state, description, target_url, repo_name, repo_owner, github_token):
    """
    Set the status "state" of a commit on GitHub using the GitHub API. 
    See section `Create a commit status` in the GitHub API documentation, or the README, for more information

    :param commit_sha: The SHA of the commit to set the status for.
    :type commit_sha: str

    :param state: The state of the status. Can be one of "pending", "success", "error" or "failure".
    :type state: str

    :param description: A short description of the status which is visible in the GitHub UI.
    :type description: str

    :param target_url: The URL to associate with this status. This URL will be linked from the GitHub UI.
    :type target_url: str

    :param repo_name: The name of the repository.
    :type repo_name: str

    :param repo_owner: The owner of the repository.
    :type repo_owner: str

    :param github_token: A GitHub token with the necessary permissions to set the status.
    :type github_token: str

    :return: The response from the GitHub API.
    :rtype: dict
    """

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/statuses/{commit_sha}"

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github+json",
    }

    if target_url != "":
        data = {
            "state": state,
            "target_url": target_url,
            "description": description
        }
    else:
        data = {
            "state": state,
            "description": description
        }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def generate_build_file(test_output, syntax_output):
    """
    Generate a log file containing both the unittest output and syntax checking output

    :param test_output: unittest output
    :type test_output: str

    :param syntax_output: syntax checking output
    :type syntax_output: str
    """

    log_file_path = "logs/test_output.log"
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    with open(log_file_path, "w") as log_file:
        log_file.write(f"Build results ({today} - {current_time}):\n\n")
        log_file.write("Unittests:\n\n")
        log_file.write(test_output)
        log_file.write("\n\nSyntax Checking:\n\n")
        log_file.write(syntax_output)


def build_results():
    """
    Used as the target_url in the GitHub API status request. Presents the 
    output of tests and syntax checking.

    :return: The content of the log file if found, otherwise an error message
    :rtype: str
    """
    
    log_file_path = "logs/test_output.log"

    if not os.path.exists(log_file_path):
        return "Log file not found", 404
    
    with open(log_file_path, "r") as log_file:
        log_content = log_file.read()

    return Response(log_content, mimetype='text/plain')


def build_application():
    """
    Execute the build command and creates a new GitHub release with the build artifacts.

    This function is a Flask POST endpoint that receives an API call from GitHub webhooks
    with merges to the branch "assessment". It executes the build command and creates a new
    GitHub release with the build artifacts.

    :return: A tuple containing a message and a status code.
    :rtype: tuple
    """

    secret_message = os.getenv('BUILD_SECRET')
    github_token = os.getenv('GITHUB_TOKEN')

    verified = verify_webhook_signature(request.data, secret_message, request.headers["X-Hub-Signature-256"])

    if not verified:
        abort(403, "x-hub-signature-256 header missing or invalid!")

    payload_data = request.json
    target_url = request.url.replace("build", "output")
    
    try:
        payload = Payload('pull_request', payload_data)
        action = payload.action
    except (KeyError, AttributeError) as error:
        print(error)
        abort(400, "Invalid payload")

    if action in ['opened', 'reopened', 'synchronize', 'edited']:
        set_status(payload.commit_sha, "pending", "Running build script", "", payload.repo_name, payload.repo_owner, github_token)
        
        try:
            repo_path, repo = _clone_repo(payload.clone_url)
        except(GitCommandError):
            return 'unable to clone repo', 400

        
        repo.git.checkout(payload.commit_sha)

        # Run syntax checking
        syntax_result_code, syntax_output = syntax_checker(repo_path)
        
        # Run tests
        test_result_code = 1
        test_output = "No tests run due to failure of syntax checking"

        if syntax_result_code == 0:
            test_result_code, test_output = run_tests(repo_path)

        generate_build_file(test_output, syntax_output)

        # Set success/failure status upon test/syntax completion
        if test_result_code == 0 and syntax_result_code == 0:
            set_status(payload.commit_sha, "success", "Build succeeded", target_url, payload.repo_name, payload.repo_owner, github_token)
        
        else:
            set_status(payload.commit_sha, "failure", "Build failed", target_url, payload.repo_name, payload.repo_owner, github_token)

        _remove_repo(repo_path)


    return "Build command executed", 200
