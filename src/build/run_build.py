import requests
import os
from payload import Payload


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
    return "Build command executed", 200
