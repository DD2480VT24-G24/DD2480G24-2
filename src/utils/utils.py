import git
import subprocess

def _clone_repo(repo_url, destination_path):
    """
    Clones a Git repository from the specified URL to the given destination path.

    Parameters:
        repo_url (str): The URL of the Git repository to clone.
        destination_path (str): The path where the repository will be cloned.

    Returns:
        None

    Raises:
        git.exc.GitCommandError: If an error occurs during the cloning process.
    """
    try:
        git.Repo.clone_from(repo_url, destination_path)
        print("Repository cloned successfully.")
    except git.exc.GitCommandError as e:
        print(f"Error cloning repository: {e}")

def _remove_repo(destination_path='temp/'):
    """
    Removes a directory or file at the specified destination path using the 'rm' command.

    Parameters:
        destination_path (str): The path to the directory or file to be removed.

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: If the subprocess call returns a non-zero exit status,
            indicating an error occurred during the removal process.
        Exception: If an unexpected error occurs during execution.

    Note:
        This function utilizes the 'rm -rf' command via subprocess to remove the specified directory
        or file. It is important to exercise caution when using this function, as it permanently
        deletes the specified content.
    """
    try:
        subprocess.run(["rm", "-rf", destination_path])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")