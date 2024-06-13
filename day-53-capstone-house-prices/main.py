import re
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from constants import *


@dataclass
class Property:
    price: str = ""
    location: str = ""
    href: str = ""


class FindHousing:
    soup: BeautifulSoup
    rent_property_list: list[Property] = []

    def __init__(self):
        response = requests.get(url=ZILLOW_ENDPOINT)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_property(self):
        willow_list = self.soup.find_all('li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')
        for i in range(len(willow_list)):
            rent_property = Property()
            price = willow_list[i].find_next('span').get_text()
            price = price.split('+')
            rent_property.price = re.sub('[^0-9]', '', price[0])
            rent_property.href = willow_list[i].find_next('a')['href']
            rent_property.location = willow_list[i].find_next('address').get_text().strip()
            self.rent_property_list.append(rent_property)
            del rent_property

    def fill_google_form(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        for property_ in self.rent_property_list:
            driver.get(GOOGLE_FORM)
            sleep(2)
            address = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(property_.location)
            price = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(str(property_.price))
            link = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(str(property_.href))
            button = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            button.click()


if __name__ == '__main__':
    app = FindHousing()
    app.get_property()
    app.fill_google_form()
