import requests

# https://sheety.co/ AND LINK GOOGLE SHEET TO GET END POINT
# CREATE SHEET NAMED "Flight Deals" WITH 3 COLUMNS - "City", "IATA Code", "Lowest Price"
SHEETY_ENDPOINT = ""


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",
                                    json=new_data)
            print(response.text)
