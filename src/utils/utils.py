import git

def _clone_repo(repo_url, destination_path):
    
    try:
        git.Repo.clone_from(repo_url, destination_path)
        print("Repository cloned successfully.")
    except git.exc.GitCommandError as e:
        print(f"Error cloning repository: {e}")