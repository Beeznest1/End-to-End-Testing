from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import BeeznestsLocators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()  # login button on the top-right of the Beeznests page
    driver.find_element(By.ID, "email").send_keys("admin@beeznests.com")
    sleep(2)
    driver.find_element(By.ID, "password").send_keys("12345678")
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()  # login button underneath the email and password fields
    sleep(2)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def PostingJob():
    driver.find_element(By.XPATH, "//span[@class='tw-uppercase']").click()  # Internship/full-time job Tab
    sleep(1.5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Post a new job']").click()  # Post a new job button
    sleep(1.5)
    driver.find_element(By.XPATH, "//div[@role='radiogroup']//div[2]//div[1]//div[1]").click()  # second radio type (paid Job)
    sleep(1.5)
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("QA Analyst")  # position title
    sleep(1.5)
    driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Apple")  # Company Name
    sleep(1.5)
    driver.find_element(By.XPATH, "(//div[@class='v-select__selections'])[1]").click()  # collage availability dropdown menu
    sleep(1.5)
    driver.find_element(By.XPATH, "(//div[@class='v-input--selection-controls__ripple'])[3]").click()
    sleep(1)
    driver.find_element(By.XPATH, "(//div[@class='row justify-center'])[1]").click()  # click anywhere on the webpage
    sleep(3)
    driver.find_element(By.XPATH, "(//div[@class='v-select__selections'])[2]").click()  # category
    sleep(1.5)
    driver.find_element(By.XPATH, "(//div[contains(text(),'Marketing')])[2]").click()  # category / marketing
    sleep(1.5)
    driver.find_element(By.XPATH, "//input[@role='button']").click()  # app deadline
    sleep(3)  # waiting is mandatory in here because of loading the elements
    driver.find_element(By.XPATH, "//div[normalize-space()='23']").click()  # selecting day
    sleep(1.5)
    driver.find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys("25")
    sleep(1)
    driver.find_element(By.XPATH, "(//p)[2]").send_keys(locators.About_the_company)
    driver.find_element(By.XPATH, "(//p)[4]").send_keys(locators.job_Description)
    driver.find_element(By.XPATH, "(//p)[6]").send_keys(locators.what_you_will_do)
    driver.find_element(By.XPATH, "(//p)[8]").send_keys(locators.Skills_you_possess)
    driver.find_element(By.XPATH, "(//p)[10]").send_keys(locators.who_you_work_with)
    sleep(2)
    driver.find_element(By.XPATH, "//span[@class='v-btn__content']").click()  # save button


Login()
PostingJob()
