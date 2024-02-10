from flask import Flask, abort, request
import requests
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from payload import Payload
from utils.utils import verify_webhook_signature


def set_status(commit_sha, state, description, target_url, repo_name, repo_owner, github_token):
    #DOCS"#######

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/statuses/{commit_sha}"

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github+json",
    }
    data = {
        "state": state,
        #"target_url": target_url,  Add target URL here when it has been implemented
        "description": description
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


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

    if 'pull_request' in payload_data:

        try:
            payload = Payload('pull_request', payload_data)
            action = payload.action
        except (KeyError, AttributeError) as error:
            print(error)
            abort(400, "Invalid payload")

        if action in ['opened', 'reopened', 'synchronize', 'edited']:
            set_status(payload.commit_sha, "pending", "Running build script", "TBD", payload.repo_name, payload.repo_owner, github_token)

            # Run tests, syntax checking etc

            # Set success/failure status upon test/syntax completion

    return "Build command executed", 200
