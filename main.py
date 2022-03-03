from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

bob = DataManager()
charlie = FlightSearch()
tommy = FlightData()
johnny = NotificationManager()

dictionary = bob.get_iata_codes()
sample_list = (charlie.find_flights(dictionary))
the_messages = tommy.organize_flights(sample_list)
johnny.send_message(the_messages)



#This file will need to use the DataManager,FlightSearch, FlightData,
#   NotificationManager classes to achieve the program requirements.


