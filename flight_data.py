class FlightData:

    def organize_flights(self, imported_list):
        message_list = []
        flight_num = 1

        for flight in imported_list:
            stopovers_dict = {}
            price = flight["data"]["price"]
            for place in flight['data'][0]['route']:
                origin = place['cityFrom']
                destination = place["cityTo"]
                time_departure_local = place["local_departure"] # Clean this up to the time alone -- split along 'T'
                # I need to get time in air, which should be UTC_Arrival - UTC_Depart.


            final_destination = flight['data'][0]['route'][0]
            home = ['cityFrom']
            for n in len(flight['route']):

            message = f"Flight: #{flight_num}. Price: ${price}" \
                      f"Route to {final_destination}: " \
                      f"{flight['route'][0]} "

            flight_num += 1

# Price,
# Date and time leaving,
# Date and time returning,
# Length of flights,
# To where,
# With which airline,
# .
