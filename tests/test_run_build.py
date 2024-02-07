import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import src.build.run_build as run_build


class TestRunBuild(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
