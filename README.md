# DD2480G24: CI
Minimum Supported Python Version (MSPV): 3.7
Test Framework: unittest (Python native module)

## Specification
An information specification of the CI server can be found in the `SPEC.md` file.

## Installation
First make sure you are in the root directory of the repository.
Create a virtual environment through `python -m venv venv`.
Activate the virtual environment by running the appropriate `activate` script in `venv/bin/`.
Install all dependencies with `python -m pip install -r requirements.txt`.
Use the `deactivate` command in your terminal when you are done.

## Documentation
Generate the documentation by running `make docs` after [installation](#Installation).
After building the documentation, a PDF is available at `docs/build/pdf`.

## Testing
The unit testing is based on the Python built in `unittest` framework (https://docs.python.org/3/library/unittest.html)

To run all tests in a file:
- `python -m unittest <path to testfile>`

## API Endpoints
### Logs
- `GET /logs/<commit_id>`: Returns the logs for the given commit id
- `GET /logs/all`: Returns all logs

The logs are stored in the `logs` directory and are named after the commit id. The logs are stored in the format `logs/<commit_id>.log`. Based on this we can retrieve the logs for a specific commit id. This endpoint will return a dict with the date of the build, the commit id and the log messages.

The `GET /logs/all` endpoint will return a list of all logs in the logs directory.

## CI Tools Documentation
### GitHub Webhooks
This implementation utilises several webhooks for different purposes, such as handling issue creation and pull requests. 
Currently, the CI server implementation is hosted locally and consequently all internet traffic is tunneled through [ngrok](https://ngrok.com). Any given Webhook in this project has the following characteristics:
- `Payload URL`: The forwarding URL provided by `ngrok`
- `Secret`: Secret message for validation of payload authenticity
- `Content type`: application/json
- `SSL verification`: Enable SSL verification
- `Events`: The event handled by the Webhook

### GitHub API
The GitHub API is used to set the status of a commit during the CI process on the server. 
The implementation requires that the environment variables `BUILD_SECRET` and `GITHUB_TOKEN`
are set, as these are required to verify GitHub webhooks as well as make requests to the
GitHub API. The method `set_status` in `run_build.py` is used to set the status of a commit to either of the
available statuses "pending", "success", "error" or "failure". The implementation follows the 
[GitHub documentation](https://docs.github.com/en/rest/commits/statuses?apiVersion=2022-11-28) under section `Create a commit status`.
