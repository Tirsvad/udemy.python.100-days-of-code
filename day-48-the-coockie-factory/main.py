import time

import continuous_threading
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
item_ids.pop()  # remove buyElder Pledge
item_ids.reverse()


def cookie_click():
    while True:
        cookie.click()


def buy_upgrade():
    while True:
        store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
        store.reverse()

        for upgrade in store:
            for itme_id in item_ids:
                valid_for_upgrade = None
                try:
                    valid_for_upgrade = upgrade.find_element(By.CSS_SELECTOR, f"#{itme_id} :not(.grayed)")
                except Exception:
                    pass
                if valid_for_upgrade:
                    driver.find_element(by=By.ID, value=itme_id).click()
        time.sleep(5)


def main():
    th = continuous_threading.ContinuousThread(target=cookie_click)
    th.start()
    th2 = continuous_threading.ContinuousThread(target=buy_upgrade)
    th2.start()
    time.sleep(300)


if __name__ == '__main__':
    main()
    result = driver.find_element(By.ID, "cps").text
    driver.quit()
    print(f"Result : {result}")
