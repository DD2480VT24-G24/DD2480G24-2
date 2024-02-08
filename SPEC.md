# Continuous Integration (CI) Server Specification

## Objective:
Develop a CI server in Python that integrates with GitHub via Webhooks to automate testing upon pull request events, building the project etc.

## Core Features:

### Webhook Receiver:
- The CI server is a Flask-based web server that listens for the configured GitHub Webhook events.
- The endpoint `/webhook` is configured to accept POST requests representing GitHub events.

### GitHub Event Validation:
- Prior to handling Webhook requests, a validation of incoming webhook events using a secret token is performed to ensure authenticity. [See Github Webhook validation](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries)
- Parses the payload to extract relevant event details like repository URL and commit SHA.

### Automated Test Execution:
- Triggers a series of automated tests when a pull request is opened or reopened.
- Utilizes the unittest framework to run test cases.
- Captures test results and outputs for further processing.

### GitHub Status Updates:
- Uses the GitHub Statuses API to set the commit status. [See Github Commit Statuses](https://docs.github.com/en/rest/commits/statuses?apiVersion=2022-11-28)
- Marks the status as pending when tests commence.
- Updates the status to success or failure upon test completion, depending on the test results, and provides the test output.

### Security and Authentication:
- Securely handles GitHub access tokens
- Ensures secure transmission of tokens via HTTPS.

### Repository Handling:
- Clones the repository using SSH to avoid credential issues during automated processes.
- Ensures cleanup of cloned repositories after tests are completed to maintain a clean server.

## Operational Flow:
1. The server receives a webhook event and validates it.
2. Upon a pull request event, the server sets the status to pending and starts the test runner.
3. After testing, the server captures the output and sets the status to success or failure.
4. The server provides test output for debugging purposes.

## Dependencies:
- Flask web framework for the HTTP server.
- requests library for making GitHub API calls.
- subprocess module for running shell commands.
- hashlib and hmac modules for verifying the signature of the hashed Webhook secret message

## Security Considerations:

Due to the security level of the GitHub API access token, as well as the secret Webhook messages, these variables are currently implemented as environment variables locally in each developers' environment.