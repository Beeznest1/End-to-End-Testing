from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import BeeznestsLocators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("admin@beeznests.com")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys("12345678")
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()  # login button
    sleep(3)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def PostProject():
    driver.find_element(By.XPATH, '/html/body/div/header/div[1]/div/nav[1]/a[1]/span').click()  # Project tab
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/a').click()  # Post A New Project button
    driver.find_element(By.XPATH, locators.position).send_keys("Software Developer")  # Position Type
    sleep(2)
    driver.find_element(By.XPATH, locators.ProjectName).send_keys("Enjoy Dude")  # Project/Company Name
    driver.find_element(By.XPATH, locators.category).click()  # Category
    driver.find_element(By.XPATH, "//div[contains(text(),'Cloud Computing Engineers')]").click()
    bar = driver.find_element(By.XPATH, "//div[@class='v-slider__thumb primary']")
    ActionChains(driver).click_and_hold(bar).pause(1).move_by_offset(230, 0).release().perform()  # move the slider
    driver.find_element(By.XPATH, locators.AppDeadline).click()  # Application Deadline
    sleep(3)
    driver.find_element(By.XPATH, "//div[normalize-space()='30']").click()  # selecting the day in the calendar
    driver.find_element(By.XPATH, locators.Project_Description).send_keys("Enjoy Dude Goal is to build a software which make people works easy")
    driver.find_element(By.XPATH, locators.What_you_will_Do).send_keys("developing the front-end code for the app")
    driver.find_element(By.XPATH, locators.Skills).send_keys("HTML, CSS, JS, SQL")
    driver.find_element(By.XPATH, locators.Who_you_work_with).send_keys("Front-End Team")
    driver.find_element(By.XPATH, locators.Experience).send_keys("it gives a good experience for the students to have more confidence in their Future Job")
    driver.find_element(By.XPATH, locators.Key_practical_skills).send_keys("developing their coding skill and improving their understanding of front-end")
    driver.find_element(By.XPATH, "//span[normalize-space()='next']").click()  # first Next Button
    driver.find_element(By.XPATH, locators.second_next_button).click()


Login()
PostProject()
