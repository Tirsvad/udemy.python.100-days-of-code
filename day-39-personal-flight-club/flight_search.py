import os
import requests

# Authorization: Bearer  6CHCFwKTpdJecJVtqgiaquOf7zDjlzrE
# api secret i6zABqR1xjdAI7l2
# url "https://test.api.amadeus.com/v1/shopping/flight-destinations"


class FlightSearch:
    token: str
    headers: dict
    endpoint: str

    def __init__(self):
        self.token = os.getenv("AMADEUS_TOKEN")
        self.headers = {
            "Authorization": self.token,

        }

        # This class is responsible for talking to the Flight Search API.

    def search(self, origin, destination, maxPrice):
        params = {
            "origin": origin,
            "maxPrice": maxPrice,
            "destination": destination
        }
        response = requests.get(url=self.endpoint, params=params, headers=self.headers)

