from datetime import datetime, timedelta
from requests import get
from json import loads
from keys import TEQUILA_API_KEY

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_HEADER = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    def __init__(self):
        self.start_date = datetime.now() + timedelta(days=7)
        self.end_date = self.start_date + timedelta(days=187)

    def find_flights(self, dictionary):
        flight_list = []
        for n, (key, val) in enumerate(dictionary.items()):
            params = {
                "fly_from": "city:DAL",
                "fly_to": key,
                "date_from": self.start_date.strftime("%d/%m/%Y"),
                "date_to": self.end_date.strftime("%d/%m/%Y"),
                "flight_type": "round",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "curr": "USD",
                "price_to": val,
                "max_fly_duration": 34,
                "one_for_city": 1,
                "max_stopover": 2,
            }

            flight_api = get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADER, params=params)
            flight_api.raise_for_status()
            flights_json = loads(flight_api.text)
            if flights_json["data"]:
                flight_list.append(flights_json)
        return flight_list
