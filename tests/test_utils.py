import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.utils.utils import _clone_repo, _remove_repo, verify_webhook_signature

class TestUtils(unittest.TestCase):
    """
    Check if repo gets cloned correctly
    """
    def test_clone_repo_gets_cloned(self):
        list = _clone_repo('git@github.com:Adasjo/DD2480G24-2.git')
        temp_dir = list[0]
        if temp_dir != None:
            contents = os.listdir(temp_dir)
            self.assertTrue(len(contents) > 0)
        else:
            self.fail('Repo wasn\'t successfully cloned')

    def test_verify_webhook_signature_correct(self):
        """
        Check that the webhook verification accepts correct signature by testing it on the example from the
        GitHub documentation on "Validating webhook deliveries" under subsection 
        "Testing the webhook payload validation"
        """

        secret = "It's a Secret to Everybody"
        payload = "Hello, World!".encode()
        signature = "sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17"

        self.assertTrue(verify_webhook_signature(payload, secret, signature))

    
    def test_verify_webhook_signature_incorrect_payload(self):
        """
        Check that the webhook verification rejects correct signature by testing the same example
        as in `test_verify_webhook_signature_correct` but with a modified payload
        """

        secret = "It's a Secret to Everybody"
        payload = "Hello World!".encode()
        signature = "sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17"

        self.assertFalse(verify_webhook_signature(payload, secret, signature))

    def test_verify_webhook_signature_incorrect_secret(self):
        """
        Check that the webhook verification rejects correct signature by testing the same example
        as in `test_verify_webhook_signature_correct` but with a modified secret
        """

        secret = "It's not a Secret to Everybody"
        payload = "Hello, World!".encode()
        signature = "sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17"

        self.assertFalse(verify_webhook_signature(payload, secret, signature))