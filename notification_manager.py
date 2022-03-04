from keys import TWILIO_KEY, TWILIO_TOKEN, TWILIO_ORIGIN_NUMBER, TWILIO_DESTINATION_NUMBER
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_KEY, TWILIO_TOKEN)

    def send_message(self, message_list):
        for text in message_list:
            client = self.client
            client.messages \
                .create(
                    body=f"{text}",
                    from_=TWILIO_ORIGIN_NUMBER,
                    to=TWILIO_DESTINATION_NUMBER
                )
