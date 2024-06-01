import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()
contents = response.text.encode(" ISO-8859-1")
soup = BeautifulSoup(contents, "html.parser")

titles = soup.find_all(name="h3", class_="title")
title_list = [title.getText() for title in titles]

title_list.reverse()

with open("./movie-list.txt", "w",  encoding="utf-8") as f:
    [f.write(f"{title}\n") for title in title_list]

