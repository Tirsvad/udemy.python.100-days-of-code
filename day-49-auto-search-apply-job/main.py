import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import *


class AutoApplyJob:
    chrome_options: webdriver.chrome.options.Options
    driver: webdriver

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--lang=en")
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def webpage_linkedin(self):
        self.driver.get(
            "https://www.linkedin.com/jobs/search/?locale=en_US&geoId=105277928"
            "&keywords=python%20developer&"
            "location=Kuala%20Lumpur%2C%20Malaysia&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=false"
        )

        time.sleep(1)

        # Click Sign in Button
        time.sleep(1)
        sign_in_button = self.driver.find_element(by=By.LINK_TEXT, value="Sign in")
        sign_in_button.click()

        time.sleep(1)

        # Sign in
        time.sleep(5)
        email_field = self.driver.find_element(by=By.ID, value="username")
        email_field.send_keys(LINKEDIN_ACCOUNT_EMAIL)
        password_field = self.driver.find_element(by=By.ID, value="password")
        password_field.send_keys(LINKEDIN_ACCOUNT_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        # Locate the apply button
        time.sleep(5)
        apply_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # If application requires phone number and the field is empty, then fill in the number.
        time.sleep(5)
        phone = self.driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Submit the application
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        submit_button.click()


if __name__ == '__main__':
    app = AutoApplyJob()
    app.webpage_linkedin()
