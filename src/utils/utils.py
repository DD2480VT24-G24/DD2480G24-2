import git

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