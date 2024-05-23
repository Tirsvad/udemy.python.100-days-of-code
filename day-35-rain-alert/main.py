import os
import requests
import pywhatkit

api_params = {
    "lat": 2.947441,
    "lon": 101.845146,
    "cnt": 4,
     "appid": os.getenv("API_KEY")  # get your owm api key from openweathermap.org and replace this
}

# Call 5 day / 3 hour forecast data
api_url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=api_url, params=api_params)
response.raise_for_status()
data = response.json()["list"]
will_rain = False
for row in data:
    if row["weather"][0]['id'] < 700:
        will_rain = True

if will_rain:
    phone_numer = os.getenv("PHONENUMBER")
    # group_id = ''
    message = "Remember umbrella. It's raining today"
    time_hour = 7
    time_minute = 5
    waiting_time_to_send = 15
    close_tab = True
    waiting_time_to_close = 2
    mode = "contact"
    # open a whatsapp web tap in browser to send message
    pywhatkit.sendwhatmsg(
        phone_no=phone_numer,
        message=message,
        time_hour=time_hour,
        time_min=time_minute,
        tab_close=close_tab,
        close_time=waiting_time_to_close
        )
