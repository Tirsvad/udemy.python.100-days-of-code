##################### Extra Hard Starting Project ######################


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from dataclasses import dataclass
import pandas as pd
import datetime as dt
import random
import smtplib
from constants_personly import *

@dataclass
class Birthday:
    name: str = None
    email: str = None
    year: int = None
    month: int = None
    day: int = None


@dataclass
class Birthdays:
    list_of_birthdays: list[Birthday]


def generate_email(receiver: str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=receiver,
            msg=f"Subject:Happy birthday\n\n{letter}"
        )


def generate_letter(name: str) -> str:
    letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file, "r") as f:
        new_letter = f.read()
    new_letter = new_letter.replace('[NAME]', name)
    print(new_letter)
    return new_letter


now = dt.datetime.now()
birthdays = Birthdays(list_of_birthdays=[])


with open(file="birthdays.csv") as f:
    file_data = pd.read_csv(f).to_dict('records')

    for birthday_data in file_data:
        birthdays.list_of_birthdays.append(Birthday(**birthday_data))


for birthday in birthdays.list_of_birthdays:
    if now.month == birthday.month and now.day == birthday.day:
        letter = generate_letter(name=birthday.name)
        generate_email(receiver=birthday.email)

