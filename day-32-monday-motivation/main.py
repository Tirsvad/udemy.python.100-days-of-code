import datetime as dt
from random import choice
from constants import *
import smtplib

now = dt.datetime.now()
weekday = now.weekday()
with open(file="quotes.txt") as f:
    quotes = f.readlines()
    print(quotes)
    quote = choice(quotes)
    print(quote)

now = dt.datetime.now()
if weekday == MONDAY:
    print("it's today")
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=EMAIL, password=PASSWORD)
    #     connection.sendmail(
    #         from_addr=EMAIL,
    #         to_addrs=EMAIL_SEND_TO,
    #         msg=f"Subject:Monday Motivation\n\n{quote}"
    #     )

