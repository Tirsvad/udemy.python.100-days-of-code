import requests
import os
from datetime import datetime


class HabitTracker:
    username: str
    token: str
    pixela_endpoint: str
    pixela_tirsvad_endpoint: str
    graphs_config: dict
    headers: dict
    graph_id: str

    def __init__(self):
        self.username = "tirsvad"
        self.graph_id = "graph1"
        self.token = os.getenv('PIXELA_TOKEN')
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.pixela_tirsvad_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs"


        self.headers = {
            "X-USER-TOKEN": self.token
        }

    def create_user(self):
        user_params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        response = requests.post(url=self.pixela_endpoint, json=user_params)

        print(response.text)

    def create_graph(self):
        response = requests.post(url=self.pixela_tirsvad_endpoint, json=self.graphs_config, headers=self.headers)

        self.graphs_config = {
            "id": self.graph_id,
            "name": "running",
            "unit": "km",
            "type": "float",
            "color": "sora"
        }

        print(response.text)

    def create_pixel(self, date, amount):
        endpoint = f"{self.pixela_tirsvad_endpoint}/{self.graph_id}"
        pixel_data = {
            "date": date,
            "quantity": f"{amount}",
        }
        request_loop = True
        while request_loop:
            response = requests.post(url=endpoint, json=pixel_data, headers=self.headers)
            if "Please retry this request." not in response:
                request_loop = False
            else:
                print("Retry create")

    def update_pixel(self, date, amount):
        endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}/{date}"
        pixel_data = {
            "quantity": str(amount)
        }
        request_loop = True
        while request_loop:
            response = response = requests.put(url=endpoint, json=pixel_data, headers=self.headers)
            if "Please retry this request." not in response:
                request_loop = False
            else:
                print("Retry update")

    def delete_pixel(self, date):
        endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}/{date}"
        request_loop = True
        while request_loop:
            response = requests.delete(url=endpoint, headers=self.headers)
            if "Please retry this request." not in response:
                request_loop = False
            else:
                print("Retry delete")


app = HabitTracker()

# My running tracker
km = 9.15
date_of_run = datetime.now()
# date = datetime(year=2024, month=5, day=28)
pixel_date = date_of_run.strftime("%Y%m%d")
app.create_pixel(date=pixel_date, amount=km)
# app.update_pixel(date=pixel_date, amount=km)
app.delete_pixel(date=pixel_date)

