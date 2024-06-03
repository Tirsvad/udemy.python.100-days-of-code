from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
print(article_count.text)
driver.quit()




#
#
# def get_events():
#     # # screenshot example
#     # event-block = driver.find_elements(By.CSS_SELECTOR, value='.event-widget')
#     # with open(file="screenshot.png", mode="wb") as f:
#     #     f.write(event-block.screenshot_as_png)
#
#     events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget div ul li')
#
#     event_dict = {}
#     c = 0
#     for event in events:
#         event_dict[c] = {
#             "time": event.find_element(By.TAG_NAME, value="time").text,
#             "name": event.find_element(By.TAG_NAME, value="a").text
#         }
#         c += 1
#
#     driver.quit()
#
#     print(f"{event_dict}")
#
#
# get_events()
