from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by=By.NAME, value="fName")
lName = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
button = driver.find_element(by=By.TAG_NAME, value="button")

fname.send_keys("Jens")
lName.send_keys("Nielsen")
email.send_keys("somethimg@gmail.com")
button.click()

