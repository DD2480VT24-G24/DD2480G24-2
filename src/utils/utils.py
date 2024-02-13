import git
from git.exc import GitCommandError
import tempfile
import shutil
import hashlib
import hmac


def _clone_repo(repo_url):
    """
    Clones a Git repository from the specified URL to a temporary directory.

    :param repo_url: The url to the repo (ssh works as well)
    :type repo_url: str

    :return: temp_dir and repo: index0: the local path to the directory if clone was successful. index1: a repo object.
    :type temp_dir: list
    
    :raises gitCommandError: If an error occurs during the cloning process.
    """

    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Clone the repository into the temporary directory
        repo = git.Repo.clone_from(repo_url, temp_dir)
        
        print("Repository cloned successfully.")
        return temp_dir, repo
    except GitCommandError as e:
        print(f"Error cloning repository: {e}")
        raise e
        
def _remove_repo(destination_path):
    """
    Removes a directory or file at the specified destination path.

    :param destination_path: The path to the directory or file to be removed.
    :type destination_path: str 
   
    :return: None

    :raises FileNotFoundError: If the specified directory or file does not exist.

    :raises PermissionError: If the user does not have permission to remove the directory or file.
    
    :raises Exception: If an unexpected error occurs during execution.
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
    """
    Verify that the webhook payload was sent from GitHub. 

    :param payload_body: contents of the payload
    :type payload_body: bytes 

    :param secret_token: Stored GitHub Webhook token/secret
    :type secret_token: str

    :param signature_header: Webhooks token/secret signature
    :type signature_header: str

    :return: Whether the signature is correct or not
    """

    if signature_header:

        hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
        
        expected_signature = "sha256=" + hash_object.hexdigest()
        
        if hmac.compare_digest(expected_signature, signature_header):
            return True
    
    return False