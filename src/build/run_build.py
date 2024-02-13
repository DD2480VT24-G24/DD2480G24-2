from flask import abort, request
import requests
import os
import sys
import logging

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


def initialize_logging(commit_sha):
    log_file_path = os.path.join("logs", f"{commit_sha}.log")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger


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

    try:
        payload = Payload('pull_request', payload_data)
        action = payload.action
    except (KeyError, AttributeError) as error:
        print(error)
        abort(400, "Invalid payload")

    logger = initialize_logging(payload.commit_sha)
    target_url = request.url.replace("build", f"logs/{payload.commit_sha}")

    if action in ['opened', 'reopened', 'synchronize', 'edited']:
        set_status(payload.commit_sha, "pending", "Running build script", "", payload.repo_name, payload.repo_owner, github_token)
        
        logger.debug(f"Build started for commit {payload.commit_sha}")

        info = _clone_repo(payload.clone_url)
        repo_path, repo = info[0], info[1]

        logger.debug(f"Cloning Repo for {payload.commit_sha}")

        repo.git.checkout(payload.commit_sha)
        logger.debug(f"Checking out commit {payload.commit_sha}")

        syntax_result_code, syntax_output = syntax_checker(repo_path)

        logger.info(f"Syntax checking completed with result code {syntax_result_code}")
        logger.debug(f"Syntax checking output: {syntax_output}")

        test_result_code = 1
        test_output = ""

        if syntax_result_code == 0:
            test_result_code, test_output = run_tests(repo_path)

            logger.info(f"Unittests completed with result code {test_result_code}")
            logger.debug(f"Unittests output: {test_output}")

        # Set success/failure status upon test/syntax completion
        if test_result_code == 0 and syntax_result_code == 0:
            set_status(payload.commit_sha, "success", "Build succeeded", target_url, payload.repo_name, payload.repo_owner, github_token)

            logger.info(f"Build completed successfully for commit {payload.commit_sha}")
        else:
            set_status(payload.commit_sha, "failure", "Build failed", target_url, payload.repo_name, payload.repo_owner, github_token)

            logger.error(f"Build failed for commit {payload.commit_sha}")

        _remove_repo(repo_path)

        logger.debug(f"Removed cloned repo for commit {payload.commit_sha}")

    return "Build command executed", 200
