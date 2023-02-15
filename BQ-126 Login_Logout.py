from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("admin@beeznests.com")
    sleep(5)
    driver.find_element(By.ID, "password").send_keys("12345678")
    sleep(5)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()
    sleep(5)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def Logout():
    driver.find_element(By.XPATH, "/html/body/div/header/div[1]/div/nav[2]/div/span/img").click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/header/div[1]/div/nav[2]/div/div/div/span").click()  # Logout button
    sleep(2)
    print("you are logout of Beeznests")


Login()
Logout()
