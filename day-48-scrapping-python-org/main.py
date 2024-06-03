from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


def get_events():
    events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

    # # screenshot example
    # with open(file="screenshot.png", mode="wb") as f:
    #     f.write(events.screenshot_as_png)
    event_dict = {}
    c = 0
    for event in events:
        event_dict[c] = {
            "time": event.find_element(By.TAG_NAME, value="time").text,
            "name": event.find_element(By.TAG_NAME, value="a").text
        }
        c += 1

    driver.quit()

    print(f"{event_dict}")


get_events()
