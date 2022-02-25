from data_manager import DataManager
from flight_search import FlightSearch

bob = DataManager()
charlie = FlightSearch()

dictionary = bob.get_iata_codes()
sample_dict = (charlie.find_flights(dictionary))
print(sample_dict[0]['data'][0]['route'][0])
print("\n This is a buffer \n")
print(sample_dict[0]['data'][0]['route'][1])


#This file will need to use the DataManager,FlightSearch, FlightData,
#   NotificationManager classes to achieve the program requirements.


