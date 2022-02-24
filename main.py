from data_manager import DataManager
from flight_search import FlightSearch

bob = DataManager()
charlie = FlightSearch()

dictionary = bob.get_iata_codes()
print(charlie.find_flights(dictionary))


#This file will need to use the DataManager,FlightSearch, FlightData,
#   NotificationManager classes to achieve the program requirements.


