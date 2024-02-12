import unittest
import sys
import os
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import src.build.run_build as run_build
from src.build.run_build import set_status, generate_build_file


class TestRunBuild(unittest.TestCase):


    def get_status(self, repo_owner, repo_name, commit_sha, github_token):
        """
        Helper function that gets the status of a commit from the GitHub API.

        :param repo_owner: The owner of the repository.
        :type repo_owner: str

        :param repo_name: The name of the repository.
        :type repo_name: str
        
        :param commit_sha: The SHA of the commit to set the status for.
        :type commit_sha: str
        
        :param github_token: A GitHub token with the necessary permissions to set the status.
        :type github_token: str

        :return: The state of the commit.
        :rtype: str
        """

        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{commit_sha}/status"

        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github+json",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        response_json = response.json()
        return response_json["state"]

    # def test_set_status(self):
    #     """
    #     Tests that the status of a commit is correctly set by setting the same commit to two different statuses.
    #     The commit used is the test commit in pull request #34.
    #     """

    #     commit_sha = "3dd1a5bac9a59dd16da3f211c95d248e285dec3e"
    #     description = "Testing"
    #     target_url = "TBD"
    #     repo_name = "DD2480G24-2"
    #     repo_owner = "Adasjo"
    #     github_token = os.getenv("GITHUB_TOKEN")

    #     set_status(commit_sha, "pending", description, target_url, repo_name, repo_owner, github_token)
    #     state = self.get_status(repo_owner, repo_name, commit_sha, github_token)
    #     self.assertEqual(state, "pending")

    #     set_status(commit_sha, "success", description, target_url, repo_name, repo_owner, github_token)
    #     state = self.get_status(repo_owner, repo_name, commit_sha, github_token)
    #     self.assertEqual(state, "success")

    def test_generate_build_file(self):
        """
        Tests that the method actually creates a log output file with correct
        contents
        """

        generate_build_file("Test success", "Syntax success")

        log_file_path = "logs/test_output.log"

        if not os.path.exists(log_file_path):
            self.fail("No log file created")

        with open(log_file_path, "r") as log_file:
            log_content = log_file.read()

        self.assertIn("Test success", log_content)
        self.assertIn("Syntax success", log_content)
        





if __name__ == '__main__':
    unittest.main()
