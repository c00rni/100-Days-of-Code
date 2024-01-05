from twilio.rest import Client

class SMSNotifier(Client):

    def __init__(self, sender_number:str, receiver_number:str, username=None, password=None, account_sid=None, region=None, http_client=None, environment=None, edge=None, user_agent_extensions=None):
        super().__init__(username, password, account_sid, region, http_client, environment, edge, user_agent_extensions)
        self._sender_number = sender_number
        self._receiver_number = receiver_number

    def sendMessage(self, message:str) -> bool:
        message = self.messages.create(
            body=message,
            from_=self._sender_number,
            to=self._receiver_number
        )
        return message.status == "queued"