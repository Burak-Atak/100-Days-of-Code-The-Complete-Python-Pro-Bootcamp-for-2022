import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_ENDPOINT = "https://api.sheety.co/ec72731e11d8f46edff38609f3e5e81a/flightDeals/prices"
        self.UPDATE_ENDPOINT = "https://api.sheety.co/ec72731e11d8f46edff38609f3e5e81a/flightDeals/prices/"

    def get_data(self):
        response = requests.get(url=self.API_ENDPOINT)
        return response.json()["prices"]

    def add_data(self, parameters):
        pass

    def update_data(self, parameters, id):
        endpoint = f"{self.UPDATE_ENDPOINT}{id}"
        response = requests.put(url=endpoint, json=parameters)
