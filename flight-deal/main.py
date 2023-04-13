# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination()

tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=(6*30))

for dest in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        dest["iataCode"],
        from_time=tomorrow,
        to_time=six_month
    )
    if flight.price < dest["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low Price! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                    f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} "
                    f"to {flight.return_date}"
        )
