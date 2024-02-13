import subprocess

def syntax_checker(repo_path):
    """
    Executes a syntax check and updates the GitHub notification based on the test results.

    This function is a Flask POST endpoint that receives an API call from GitHub webhooks
    with changes from all pull requests. It runs the tests and updates the GitHub notification
    to indicate whether the application has passed the syntax check.

    :return: A tuple containing a status code and a message
    :rtype: tuple
    """
    
    results = subprocess.run(['pyright', 'src/', 'test/'], capture_output=True, text=True)
    return results.returncode, results.stdout
    