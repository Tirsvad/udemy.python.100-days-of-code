import os


class DataManager:
    endpoint: str
    token: str
    headers: dict
    data: dict
    data_list: list

    def __init__(self):
        self.endpoint = os.getenv("SHEET_ENDPOINT")
        self.token = os.getenv("SHEET_TOKEN")
        self.headers = {
            "Authorization": self.token
        }
        # response = requests.get(url=self.endpoint, headers=self.headers)
        # response.raise_for_status()
        # self.data = response.json()
        # self.data_list = self.data["prices"]
        self.data_list = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
                {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
                {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]

    # This class is responsible for talking to the Google Sheet.
