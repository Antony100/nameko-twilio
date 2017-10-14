from nameko.rpc import rpc
from nameko_twilio import Twilio


class SmsService:
    name = "sms_service"
    twilio = Twilio()

    @rpc
    def send_message(self, message, to):
        self.twilio.messages.create(
            to=to,
            from_="+441293344603",
            body=message
        )
