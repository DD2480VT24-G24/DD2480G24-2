import subprocess


def run_tests(repo_path):
    """
    This function is called from the Flask POST endpoint /build that receives an API call from GitHub webhooks
    with changes from a pull requests. It then runs the tests on the specific commit.

    :return: A tuple containing a message and a status code.
    :rtype: tuple
    """

    test_dir = f"{repo_path}/tests"
    test_pattern = 'test*.py'

    command = ["python", "-m", "unittest", "discover", "-s", test_dir, "-p", test_pattern, "-v"]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    # Get the output and return code
    output = process.stdout
    return_code = process.returncode

    return return_code, output
    