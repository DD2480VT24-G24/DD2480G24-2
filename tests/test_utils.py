import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.utils.utils import _clone_repo, _remove_repo

class TestUtils(unittest.TestCase):
    """
    Check if repo gets cloned correctly
    """
    def test_clone_repo_gets_cloned(self):
        temp_dir = _clone_repo('git@github.com:Adasjo/DD2480G24-2.git')
        if temp_dir != None:
            contents = os.listdir(temp_dir)
            self.assertTrue(len(contents) > 0)
        else:
            self.fail('Repo wasn\'t successfully cloned')