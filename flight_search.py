from datetime import datetime, timedelta
from requests import get
from json import loads
from keys import TEQUILA_API_KEY

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_HEADER = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch():
    def __init__(self):
        self.start_date = datetime.now() + timedelta(days=7)
        self.end_date = self.start_date + timedelta(days=187)

    def find_flights(self, dictionary):
        for n, (key, val) in enumerate(dictionary.items()):
            params = {
                "fly_from": "city:DAL",
                "fly_to": key,  # This needs to populate from data_manager
                "date_from": self.start_date.strftime("%d/%m/%Y"),
                "date_to": self.end_date.strftime("%d/%m/%Y"),
                "flight_type": "round",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "curr": "USD",
                "price_to": val,  # This needs to populate from data_manager
                "max_fly_duration": 34,
                "one_for_city": 1,
            }

            flights_json = loads(get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADER, params=params).text)
            print(flights_json)