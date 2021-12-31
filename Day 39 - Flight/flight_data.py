import requests


class FlightData:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.key = "FGqryPc6FIg13SyasGw2KgBiYTViFdcS"
        self.header = {
            "apikey": self.key
        }

    def search_flight(self, city, date_from, date_to):
        parameters = {
            "fly_from": "city:IST",
            "fly_to": city,
            "date_from": date_from,
            "date_to": date_to,
            "flight_type": "oneway",
            "one_for_city": 1,
            "curr": "TRY"
        }

        response = requests.get(url=self.endpoint, params=parameters, headers=self.header)

        try:
            data = response.json()["data"][0]

        except IndexError:
            print(f"No flights found for {city}.")
            return False

        flight_data = {"price": data["price"],
                       # "origin_city": data["route"][0]["cityFrom"],
                       "origin_airport": data["route"][0]["flyFrom"],
                       # "destination_city": data["route"][0]["cityTo"],
                       "destination_airport": data["route"][0]["flyTo"],
                       "out_date": data["route"][0]["local_departure"].split("T")[0]
                       }
        return flight_data
