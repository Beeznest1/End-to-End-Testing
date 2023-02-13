from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import BeeznestsLocators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://test.beeznests.com/")


def Login(password):
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("rashed.mahazi@gmail.com")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys(password)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()  # login button
    sleep(3)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def change_password():
    driver.find_element(By.XPATH, locators.DropDown_Menu).click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Change Password']").click()
    driver.find_element(By.XPATH, locators.Old_password).send_keys("12345679")
    driver.find_element(By.XPATH, locators.New_password).send_keys("12345678")
    driver.find_element(By.XPATH, locators.Confirm_new_password).send_keys("12345678")
    driver.find_element(By.XPATH, "//span[@class='v-btn__content']").click()
    sleep(3)


Login("123456789")
change_password()
# Login("12345678") # login with the new password