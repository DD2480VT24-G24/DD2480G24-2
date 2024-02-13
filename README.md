# DD2480G24: CI

## Testing
The unit testing is based on the Python built in `unittest` framework (https://docs.python.org/3/library/unittest.html)

To run all tests in a file:
- `python -m unittest <path to testfile>`


## GitHub Webhooks
This implementation utilises several webhooks for different purposes, such as handling issue creation and pull requests. 
Currently, the CI server implementation is hosted locally and consequently all internet traffic is tunneled through [ngrok](https://ngrok.com). Any given Webhook in this project has the following characteristics:
- `Payload URL`: The forwarding URL provided by `ngrok`
- `Secret`: Secret message for validation of payload authenticity
- `Content type`: application/json
- `SSL verification`: Enable SSL verification
- `Events`: The event handled by the Webhook

## GitHub API
The GitHub API is used to set the status of a commit during the CI process on the server. 
The implementation requires that the environment variables `BUILD_SECRET` and `GITHUB_TOKEN`
are set, as these are required to verify GitHub webhooks as well as make requests to the
GitHub API. The method `set_status` in `run_build.py` is used to set the status of a commit to either of the
available statuses "pending", "success", "error" or "failure". The implementation follows the 
[GitHub documentation](https://docs.github.com/en/rest/commits/statuses?apiVersion=2022-11-28) under section `Create a commit status`.

## Contributions
**Adam**

**Andreas**
- Repo Admin (issues, pull requests, labeling, etc.)
- Miscellaneous help (subsitute pair programmer, debugging, advice, etc.) with all group members
- Documentation management (Misc. fixes, restructuring/writing, fill in blanks)

**Casper**

**Martin**

**Victor**
