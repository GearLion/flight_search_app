from requests import get
from json import loads
from keys import SHEETY_BASE8_PASSWORD

sheety_endpoint = "https://api.sheety.co/adb041be0364f24d148351b1aa8c6fb7/cheapFlights/flightList"

header = {
    "Authorization": SHEETY_BASE8_PASSWORD,
}

flight_data = get(url=sheety_endpoint, headers=header)
flight_dict = loads(flight_data.text)


for n, val in enumerate(flight_dict["flightList"]):
    print(flight_dict["flightList"][n]["iataCode"])


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass