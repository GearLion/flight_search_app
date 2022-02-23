from datetime import datetime, timedelta
from requests import get
from keys import TEQUILA_API_KEY

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

header = {
    "apikey": TEQUILA_API_KEY,
}

today = datetime.now() + timedelta(days=7)
end_date = today + timedelta(days=187)


params = {
    "fly_from": "city:DAL",
    "fly_to": "MNL",  # This needs to populate from data_manager
    "date_from": today.strftime("%d/%m/%Y"),
    "date_to": end_date.strftime("%d/%m/%Y"),
    "flight_type": "round",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 31,
    "curr": "USD",
    "price_to": 1400,  # This needs to populate from data_manager
}

response = get(url=TEQUILA_ENDPOINT, headers=header, params=params)
print(response.text)


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass