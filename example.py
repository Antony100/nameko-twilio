from nameko.rpc import rpc
from nameko_twilio import Twilio


class MessageService:
    name = "message_service"
    twilio = Twilio()

    @rpc
    def send_message(self, message, to):
        self.twilio.messages.create(
            to=to,
            from_="YOUR TWILIO NUMBER HERE",
            body=message
        )
