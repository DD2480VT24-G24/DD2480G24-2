import os
import datetime
from flask import jsonify, abort


def get_log_individual(id):
    """
    Retrieves the log file for a given ID and returns its contents along with metadata.

    Args:
        id (str): The ID of the log file.

    Returns:
        dict: A dictionary containing the commit ID, last modified date, and log contents.

    Raises:
        404 Error: If the log file does not exist.
    """
    log_file = f'logs/{id}.log'

    if not os.path.exists(log_file):
        abort(404)

    last_modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(log_file)).isoformat()

    with open(log_file, 'r') as file:
        log = file.read()

    return jsonify({
        "commit": id,
        "date": last_modified_date,
        "log": log
    })
