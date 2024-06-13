from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import *


class InternetSpeedXBot:
    driver: webdriver
    up: float
    down: float

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_ENDPOINT)
        sleep(2)
        try:
            button = self.driver.find_element(By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")

        except NoSuchElementException:
            pass
        else:
            button.click()

        start_speed_test = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        start_speed_test.click()
        sleep(60)

        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)

    def x_at_provider(self):
        self.driver.get(X_ENDPOINT)
        sleep(2)
        username_field = self.driver.find_element(
            By.XPATH,
            '//*[@autocomplete="username"]'
        )
        username_field.send_keys(X_EMAIL, Keys.ENTER)
        print(username_field)
        password_field = self.driver.find_element(
            By.XPATH,
            '//*[@autocomplete="current-password"]'
        )
        password_field.send_keys(X_PASSWORD, Keys.ENTER)

if __name__ == '__main__':
    app = InternetSpeedXBot()
    # app.get_internet_speed()
    app.x_at_provider()
