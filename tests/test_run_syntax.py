import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import src.syntax.run_syntax as run_syntax


class TestRunSyntax(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
