import os, sys
import unittest
import io
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


def run_tests(repo_path):
    """
    This function is called from the Flask POST endpoint /build that receives an API call from GitHub webhooks
    with changes from a pull requests. It then runs the tests on the specific commit.

    :return: A tuple containing a message and a status code.
    :rtype: tuple
    """

    test_dir = f"{repo_path}/tests"
    test_pattern = 'test*.py'

    test_output = io.StringIO()

    test_suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern=test_pattern)
    test_runner = unittest.TextTestRunner(stream=test_output, verbosity=2)
    
    result = test_runner.run(test_suite)

    if result.wasSuccessful():
        return 0, test_output.getvalue()
    
    return 1, test_output.getvalue()
