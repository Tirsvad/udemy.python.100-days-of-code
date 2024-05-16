import requests
from dataclasses import dataclass
import datetime as dt


@dataclass
class IssPosition:
    timestamp: int
    latitude: float
    longitude: float


@dataclass
class TrackIssPositions:
    iss_position: list[IssPosition] | list


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

position = IssPosition(
    timestamp=data['timestamp'],
    longitude=data['iss_position']['longitude'],
    latitude=data['iss_position']['latitude']
)

new = TrackIssPositions(iss_position=[])
new.iss_position.append(position)


print(f"https://www.latlong.net/c/?lat={data['iss_position']['latitude']}&long={data['iss_position']['longitude']}")


# Python program to convert time
# from 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12

    if str1[1:2] == ":":
        str1 = "0" + str1

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

        # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

        # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


def get_sunset(latitude, longitude):
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}")
    response.raise_for_status()
    data = response.json()
    return data


now = dt.datetime.now()
iss_datetime = dt.datetime.fromtimestamp(data['timestamp'])

# datetime.timestamp(now)
view_time = get_sunset(latitude=data['iss_position']['latitude'],longitude=data['iss_position']['longitude'])
astronomical_twilight_end = view_time['results']['astronomical_twilight_end']
astronomical_twilight_begin = view_time['results']['astronomical_twilight_begin']
# convert24(astronomical_twilight_end)
astronomical_twilight_end = convert24(astronomical_twilight_end).strip()
astronomical_twilight_begin = convert24(astronomical_twilight_begin).strip()

astronomical_twilight_end = dt.datetime.strptime(astronomical_twilight_end, r"%H:%M:%S")
astronomical_twilight_end = astronomical_twilight_end.replace(year=now.year, month=now.month, day=now.day)

astronomical_twilight_begin = dt.datetime.strptime(astronomical_twilight_begin, r"%H:%M:%S")
astronomical_twilight_begin = astronomical_twilight_begin.replace(year=now.year, month=now.month, day=now.day)

print(astronomical_twilight_begin.timestamp())
print(now.timestamp())
print(astronomical_twilight_end.timestamp())
print(astronomical_twilight_end.timestamp() < now.timestamp())
print(now.timestamp() < astronomical_twilight_begin.timestamp())

if not astronomical_twilight_end.timestamp() < now.timestamp() < astronomical_twilight_begin.timestamp():
    print("you can see ISS Station on the sky")
else:
    print("ISS Station is on the sky over you but you can see it at day time!")


