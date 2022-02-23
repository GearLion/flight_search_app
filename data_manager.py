from requests import get
from json import loads
from keys import SHEETY_BASE8_PASSWORD

sheety_endpoint = "https://api.sheety.co/adb041be0364f24d148351b1aa8c6fb7/cheapFlights/flightList"
header = {
    "Authorization": SHEETY_BASE8_PASSWORD,
}


class DataManager:
    def __init__(self):
        self.flight_data = loads(get(url=sheety_endpoint, headers=header).text)

    def get_iata_codes(self):
        places = {}
        for n, val in enumerate(self.flight_data["flightList"]):
            iata_code = self.flight_data["flightList"][n]["iataCode"]
            price = self.flight_data["flightList"][n]["lowestPrice"]
            places[iata_code] = price
        return places
