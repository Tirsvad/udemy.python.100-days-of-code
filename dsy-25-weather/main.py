# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
#
# temp_average = data["temp"].mean()
# temp_max = data["temp"].max()
#
# print(temp_max)


# print(data[data.temp == data["temp"].max()])

# monday = data[data["day"] == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)


data_dict = {
    "students": ["Neisa", "Victoria", "Carl"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
