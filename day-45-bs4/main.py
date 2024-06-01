from typing import Dict, Any

from bs4 import BeautifulSoup
import requests
import operator

url = "https://news.ycombinator.com/newest"
response = requests.get(url=url)
response.raise_for_status()
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")

articles_list = [
    {
        "text": articles[index].getText(),
        "link": articles[index].find(name="a").get("href"),
        "score": int(scores[index].getText().split(" ")[0])
     }
    for index in range(len(scores))]

articles_list_sorted = []
[articles_list_sorted.append(dict_sorted) for dict_sorted in sorted(
    articles_list,
    key=operator.itemgetter("score"),
    reverse=True
)]

print("Score    Article\n")
for article in articles_list_sorted:
    print(f"{article['score']:<8} {article['text']}")
    print(f"{article['link']:<8}\n")
