from nameko.extensions import DependencyProvider
from twilio.rest import Client


class Twilio(DependencyProvider):

    def setup(self):
        self.twilio_account_sid = self.container.config['account_sid']
        self.twilio_auth_token = self.container.config['auth_token']

    def start(self):
        self.client = Client(
            self.twilio_account_sid, self.twilio_auth_token
        )

    def get_dependency(self, worker_ctx):
        return self.client

    def stop(self):
        self.client = None
