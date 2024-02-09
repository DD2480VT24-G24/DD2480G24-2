class Payload:
    
    def __init__(self, payload_type, payload_dict):
        self.payload_type = payload_type
        self.payload = payload_dict

        self.parse_payload()

    def parse_payload(self):
        if self.payload_type == 'pull_request':
            self.action = self.payload["action"]
            self.clone_url = self.payload['pull_request']['head']['repo']['ssh_url']
            self.repo_owner = self.payload['repository']['owner']['login']
            self.repo_name = self.payload['pull_request']['head']['repo']['name']
            self.commit_sha = self.payload['pull_request']["head"]["sha"]


