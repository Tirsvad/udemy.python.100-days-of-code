import pandas as pd

DATA_PATH = "data"
DATA_FILE = f"{DATA_PATH}/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
DATA_NEW_FILE = f"{DATA_PATH}/squirrel_count.csv"
count_list = []
data = pd.read_csv(DATA_FILE)
colors = data["Primary Fur Color"].dropna().unique()

data_dict = {
    "Fur Color": colors
}

for color in colors:
    count_list.append(data["Primary Fur Color"][data["Primary Fur Color"] == color].count())

data_dict.update({"Count": count_list})

df = pd.DataFrame(data_dict)
df.to_csv(DATA_NEW_FILE)
