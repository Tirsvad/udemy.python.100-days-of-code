import os
from datetime import datetime

import requests

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercise did you today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

data = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 96.6,
    "height_cm": 180,
    "age": 49
}

response = requests.post(url=exercise_endpoint, json=data, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

sheet_endpoint = os.getenv("SHEET_ENDPOINT")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers_sheet = {
        "Authorization": os.getenv("SHEET_TOKEN")
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers_sheet)

    print(sheet_response.text)
