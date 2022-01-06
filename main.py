from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

item_names = [
    "Cursor",
    "Grandma",
    "Factory",
    "Mine",
    "Shipment",
    "Alchemy lab",
    "Portal",
    "Time machine",
    "Elder Pledge"
]
items = [None] * len(item_names)
cookie = driver.find_element(By.ID, "cookie")


def click_cookie(seconds):
    stop_time = time.time() + seconds
    count = 0
    while stop_time > time.time():
        count += 1
        cookie.click()
    print(f'{count / seconds} clicks per second')


def buy_most_expensive_item():
    for i in range(len(items)):
        items[i] = driver.find_element(By.ID, "buy" + item_names[i])
    for i in range(len(items) - 1, -1, -1):
        if items[i].get_attribute("class") == "":
            items[i].click()
            break


run_time = time.time() + 5*60  # 5 minute run
delay = 5.0  # Initial seconds
while run_time > time.time():
    click_cookie(seconds=delay)
    buy_most_expensive_item()
driver.get_screenshot_as_file("screenshot.png")

driver.close()

