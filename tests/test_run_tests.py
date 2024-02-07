import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import tests.run_tests as run_tests


class TestRunTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
