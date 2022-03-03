from datetime import datetime, timedelta
# Add layover times.


class FlightData:

    def organize_flights(self, flight_list):
        message_list = []
        flight_num = 1
        arrival_time = 0

        for flight in flight_list:
            # Organize Info for Each Leg
            flights_text = ""
            leg_time = []
            go_flight_time = 0
            return_flight_time = 0
            leg_num = 1
            for leg, place in enumerate(flight['data'][0]['route']):
                origin = place['cityFrom']
                destination = place["cityTo"]
                time_departure_local = place["local_departure"].split("T")[1].split(".")[0]
                departure_utc = place["utc_departure"].split(".")[0]
                if leg == 0:
                    flights_text += "Go Flight Info:\n"
                time_arrival_local = place["local_arrival"].split("T")[1].split(".")[0]
                arrival_utc = place["utc_arrival"].split(".")[0]
                time_in_air = datetime.strptime(arrival_utc, "%Y-%m-%dT%H:%M:%S") - datetime.\
                    strptime(departure_utc, "%Y-%m-%dT%H:%M:%S")
                if arrival_time == 0:
                    arrival_time = arrival_utc
                else:
                    layover_time = datetime.strptime(departure_utc, "%Y-%m-%dT%H:%M:%S") - datetime. \
                        strptime(arrival_time, "%Y-%m-%dT%H:%M:%S")
                    layover_text = f"    Layover Time:   {layover_time}\n"
                    arrival_time = arrival_utc
                leg_time.append(time_in_air)
                if place['cityTo'] == flight['data'][0]['cityTo']:
                    go_flight_time = sum(leg_time, timedelta())
                    leg_time.clear()
                    arrival_time = 0
                    return_text = "\nReturn Flight Info:\n"
                elif leg == len(flight['data'][0]['route']) - 1:
                    return_flight_time = sum(leg_time, timedelta())
                this_flight = f"  Leg #{leg_num}:\n" \
                              f"    From {origin} to {destination}\n" \
                              f"    Departure Time: {time_departure_local}\n" \
                              f"    Arrival Time:   {time_arrival_local}\n" \
                              f"    Time in Air:    {time_in_air}\n"
                flights_text += this_flight
                leg_num += 1

                try:
                    flights_text += layover_text
                except UnboundLocalError:
                    pass
                try:
                    flights_text += return_text
                except UnboundLocalError:
                    pass
                else:
                    del return_text
                    del layover_text
                    leg_num = 1
            flight_num += 1

            # Add It to Info About Whole Trip
            final_destination = flight['data'][0]['cityTo']
            price = flight["data"][0]["price"]
            home = flight['data'][0]['cityFrom']

            message = f"Flight: #{flight_num},\n" \
                      f"From: {home}\n" \
                      f"Route to {final_destination}\n" \
                      f"Price: ${price}\n" \
                      f"Go Flight Time: {go_flight_time}\n" \
                      f"Return Flight Time: {return_flight_time}\n\n"
            message += flights_text
            flight_num += 1
            message_list.append(message)

        return message_list
