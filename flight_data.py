from datetime import datetime


class FlightData:

    def organize_flights(self, flight_list):
        message_list = []
        flight_num = 1

        for flight in flight_list:
            # Organize Info for Each Leg
            flights_text = ""
            for leg, place in enumerate(flight['data'][0]['route']):
                origin = place['cityFrom']
                destination = place["cityTo"]
                time_departure_local = place["local_departure"].split("T")[1].split(".")[0]
                departure_utc = place["utc_departure"].split(".")[0]
                if leg == 0:
                    first_departure = departure_utc
                time_arrival_local = place["local_arrival"].split("T")[1].split(".")[0]
                arrival_utc = place["utc_arrival"].split(".")[0]
                if leg == len(flight['data'][0]['route']):
                    final_arrival = arrival_utc
                time_in_air = datetime.strptime(arrival_utc, "%Y-%m-%dT%H:%M:%S") - datetime.\
                    strptime(departure_utc, "%Y-%m-%dT%H:%M:%S")
                this_flight = f"  Leg #{leg + 1}:\n" \
                              f"    From {origin} to {destination}\n" \
                              f"    Departure Time: {time_departure_local}\n" \
                              f"    Arrival Time:   {time_arrival_local}\n" \
                              f"    Time in Air:    {time_in_air}\n"
                flights_text += this_flight

            # Add It to Info About Whole Trip
            final_destination = flight['data'][0]['route'][0]
            price = flight["data"]["price"]
            home = flight['cityFrom']
            total_time = datetime.strptime(final_arrival, "%Y-%m-%dT%H:%M:%S") - datetime\
                .strptime(first_departure, "%Y-%m-%dT%H:%M:%S")

            message = f"Flight: #{flight_num},\n" \
                      f"From: {home}\n" \
                      f"Route to {final_destination}\n" \
                      f"Price: ${price}\n" \
                      f"Total Time: {total_time}\n"
            message += flights_text
            flight_num += 1
            message_list.append(message)

        return message_list
