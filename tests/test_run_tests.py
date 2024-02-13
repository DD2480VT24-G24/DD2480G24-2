import unittest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.utils.run_tests import run_tests


class TestRunTests(unittest.TestCase):
    
    def test_run_tests_accepts(self):
        """
        Tests that the run_tests function accepts a path to a directory containing passing tests, and passes
        all of them.
        """
        
        current_dir = os.path.dirname(os.path.abspath(__file__)) + "/../src/dummycode"

        return_code, output = run_tests(current_dir)

        self.assertEqual(return_code, 0)
        self.assertNotEqual(output, "")



if __name__ == '__main__':
    unittest.main()
