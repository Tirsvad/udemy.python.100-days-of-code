import requests
from bs4 import BeautifulSoup
import smtplib
from lxml import etree
from constants import *

response = requests.get(url=PRODUCT_END_POINT, params=PARAMS, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find_all(name="span", attrs={"class": "a-offscreen"})[1].getText().split("$")[1]

print(price)

# if float(price[1]) < 89:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=EMAIL_USER, password=PASSWORD)
#         connection.sendmail(
#             from_addr=EMAIL_FROM,
#             to_addrs=EMAIL_SEND_TO,
#             msg=f"Subject:Product on amazon now under the price setting\n\n{PRODUCT_END_POINT} at price {price}"
#         )