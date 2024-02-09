import git
import tempfile
import shutil
import hashlib
import hmac

def _clone_repo(repo_url):
    """
    Clones a Git repository from the specified URL to a temporary directory.

    Parameters:
        repo_url (str): The URL of the Git repository to clone.

    Returns:
        tmp_dir (str): The path of the temporary directory where the repository is cloned.
        None: If an error occurs during the cloning process.
    
    Raises:
        git.exc.GitCommandError: If an error occurs during the cloning process.
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Clone the repository into the temporary directory
        git.Repo.clone_from(repo_url, temp_dir)
        
        print("Repository cloned successfully.")
        return temp_dir
    except git.exc.GitCommandError as e:
        print(f"Error cloning repository: {e}")
        return None

def _remove_repo(destination_path):
    """
    Removes a directory or file at the specified destination path.

    Parameters:
        destination_path (str): The path to the directory or file to be removed.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified directory or file does not exist.
        PermissionError: If the user does not have permission to remove the directory or file.
        Exception: If an unexpected error occurs during execution.
    """
    try:
        # Remove the temporary directory
        shutil.rmtree(destination_path)
    except FileNotFoundError:
        print(f"Error: {destination_path} not found.")
    except PermissionError:
        print(f"Error: Permission denied to remove {destination_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def verify_webhook_signature(payload_body, secret_token, signature_header):
    

    if signature_header:

        hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
        
        expected_signature = "sha256=" + hash_object.hexdigest()
        
        if hmac.compare_digest(expected_signature, signature_header):
            return True
    
    return False