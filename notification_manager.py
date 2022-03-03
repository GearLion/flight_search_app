from keys import TWILIO_KEY, TWILIO_TOKEN, TWILIO_ORIGIN_NUMBER, TWILIO_DESTINATION_NUMBER
from twilio.rest import Client

class NotificationManager:

    def send_message(self, message_list):
        for text in message_list:
            client = Client(TWILIO_KEY, TWILIO_TOKEN)
            client.messages \
                .create(
                body=f"{text}",
                from_= TWILIO_ORIGIN_NUMBER,
                to= TWILIO_DESTINATION_NUMBER
            )
