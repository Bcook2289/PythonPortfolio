import requests
from flight_data import FlightData

# https://tequila.kiwi.com/portal/docs/tequila_api
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = ""


class FlightSearch:
    def get_destination_code(self, city_name):

        headers = {"apikey": TEQUILA_API_KEY}

        tequila_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true"

        }

        code = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=tequila_params)
        code = code.json()
        city_code = code["locations"][0]["city"]["code"]
        return city_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}

        query_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max)stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query_params)
        try:
            data = response.json()
            data = data["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][0]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
