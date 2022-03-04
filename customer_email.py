from keys import SHEETY_BASE8_PASSWORD
from requests import post, get
from json import loads
import smtplib
from keys import EMAIL_ADDRESS, EMAIL_PASSWORD


class CustomerEmail:
    def __init__(self):
        self.users_endpoint = "https://api.sheety.co/adb041be0364f24d148351b1aa8c6fb7/cheapFlights/users"
        self.header = {
        "Authorization": SHEETY_BASE8_PASSWORD,
    }

    def collect_emails(self):
        f_name = input("Please enter your first name.\n").capitalize()
        l_name = input("Please enter your surname.\n").capitalize()
        email = input("Please enter your email.\n")
        match = input("Please re-enter your email address.\n")
        match_email = False

        while not match_email:
            if email == match:
                match_email = True
            else:
                print("I'm sorry, the emails you entered did not match.")
                email = input("Please enter your email.\n")
                match = input("Please re-enter your email address.\n")

        params = {
            "user": {
                "first": f_name,
                "last": l_name,
                "email": email
            }
        }

        post(url=self.users_endpoint, json=params, headers=self.header)

    def send_email(self, message_list):
        email_text = ""
        for message in message_list:
            email_text += message
        user_data = loads(get(url=self.users_endpoint, headers=self.header).text)
        for user in user_data['users']:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
                connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=user['email'],
                                    msg=f"Subject: Your Tickets!\n\n"
                                        f"Dear {user['first']} {user['last']}\n{email_text}.")
