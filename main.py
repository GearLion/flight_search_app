from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

bob = DataManager()
charlie = FlightSearch()
tommy = FlightData()

dictionary = bob.get_iata_codes()
sample_list = (charlie.find_flights(dictionary))
print(sample_list)
for message in tommy.organize_flights(sample_list):
    print(message)


#This file will need to use the DataManager,FlightSearch, FlightData,
#   NotificationManager classes to achieve the program requirements.


