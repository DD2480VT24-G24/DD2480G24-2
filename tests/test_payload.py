import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.payload import Payload


class TestRunBuild(unittest.TestCase):
    
    
    def test_payload_parser_works(self):
        """
        Tests that the payload parser correctly identifies the important fields in the payload.
        The example is based on the descripion of the pull request webhook payload in the 
        GitHub "Webhook events and payloads" documentation
        """
        
        payload_example = {
            "action": "opened",
            "number": 9,
            "pull_request": {
                "url": "example.com",
                "id": 8,
                "node_id": 10,
                "html_url": "example2.com",
                "diff_url": "examplediff.com",
                "head": {
                    "repo": {
                        "archive_url": "test.com",
                        "assignees_url": "test2.com",
                        "ssh_url": "clone.com",
                        "name": "Test Repo",
                    },
                    "sha": "a2bcendoajrti"
                },
            },
            "repository": {
                "owner": {
                    "login": "Lindefor"
                }
            }
        }

        payload = Payload("pull_request", payload_example)

        self.assertEqual(payload.payload_type, 'pull_request')
        self.assertEqual(payload.action, 'opened')
        self.assertEqual(payload.clone_url, 'clone.com')
        self.assertEqual(payload.repo_owner, 'Lindefor')
        self.assertEqual(payload.repo_name, 'Test Repo')
        self.assertEqual(payload.commit_sha, 'a2bcendoajrti')


if __name__ == '__main__':
    unittest.main()
