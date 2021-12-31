from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()

# Get data from sheet
sheet_data = data.get_data()

data_flight = FlightData()
notification = NotificationManager()

date_from = "01/06/2022"
date_to = "31/12/2022"

email_message = ""
is_send_email = False

for row in sheet_data:
    city = row["iataCode"]
    id = row["id"]
    first_price = row["lowestPrice"]

    # Get flight data
    flight_data = data_flight.search_flight(city, date_from, date_to)

    if not flight_data:
        continue

    new_price = flight_data["price"]
    origin_airport = flight_data["origin_airport"]
    destination_airport = flight_data["destination_airport"]
    out_date = flight_data["out_date"]

    if new_price < first_price:
        is_send_email = True
        parameters = {
            "price": {
                "lowestPrice": new_price,
                "flightDate": out_date,
                "originAirport": origin_airport,
                "destinationAirport": destination_airport
            }
        }

        email_message += f"{city} flight price updated. New flight's price: {new_price} date: {out_date}.\n"

        # Update sheet
        data.update_data(parameters, id)

# Send email
if is_send_email:
    notification.send_email(email_message)

