from datetime import datetime, timedelta
from requests import get
from json import loads
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
    "price_to": 1500,  # This needs to populate from data_manager
    "max_fly_duration": 34,
    "one_for_city": 1,
}

response = loads(get(url=TEQUILA_ENDPOINT, headers=header, params=params).text)
print(response)
print("\n This is a break \n")
# It's nice that I've managed to pull out where we're flying to and for what price, but that information needs to be
#   added within the parameters, not here. Here is where I need to extract the data. Or... perhaps I just need to return
#   the response. Isn't '/flight_data.py' supposed to be where I organize the data into something legible?
#   Why not here?
print(response["data"][0]["flyTo"])
print(response["data"][0]["price"])

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass