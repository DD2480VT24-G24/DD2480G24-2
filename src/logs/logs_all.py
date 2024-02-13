import os


def get_log_ids():
    """
    Retrieves the IDs of all available log files.

    Returns:
        dict: A dictionary containing a list of log IDs.
    """

    log_files = os.listdir('logs/')
    log_ids = [file[:-4] for file in log_files if file.endswith('.log')]

    return {"ids": log_ids}
