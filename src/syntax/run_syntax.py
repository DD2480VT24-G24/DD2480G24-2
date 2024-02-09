import subprocess
import os

def syntax_checker():
    """
    Executes a syntax check and updates the GitHub notification based on the test results.

    This function is a Flask POST endpoint that receives an API call from GitHub webhooks
    with changes from all pull requests. It runs the tests and updates the GitHub notification
    to indicate whether the application has passed the syntax check.

    :return: A tuple containing a message and a status code.
    :rtype: tuple
    """
 #   path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    results = subprocess.run(['pyright'], capture_output=True, text=True)

    #check if pyright succeeded
    if results.returncode == 0:
        return "Static syntax check executed successfully", 200
    else:
        return f"Static syntax check failed with error: {results.stdout}", 500
