class FlightData:


    def organize_flights(self, list):
        message_list = []
        flight_num = 1
        for flight in list:
            message = f"Flight: #{flight_num}\n " \
                      f"Price: {flight['price']}" \
                      f"Departure: "

            flight_num += 1

# Price,
# Date and time leaving,
# Date and time returning,
# Length of flights,
# To where,
# With which airline,
# .
