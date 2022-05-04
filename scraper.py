from json.tool import main
from turtle import pd
import turtle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def log_in(driver):
    brown_username = os.environ["BROWN_USER"]
    brown_password = os.environ["BROWN_PASS"]
    main_window = driver.window_handles[0]
    login_window = driver.window_handles[1]
    driver.switch_to.window(login_window)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(brown_username)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(brown_password)
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]")
    login_button.click()
    driver.switch_to.window(main_window)
    # Manually complete Duo 2FA
    WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(1))

service = Service("./chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://cab.brown.edu")

# Select first department on the list
department_dropdown = driver.find_element(By.ID, "crit-dept")
department_selector = Select(department_dropdown)
department_selector.select_by_index(1)
find_courses_form = driver.find_element(By.ID, "search-form")
find_courses_form.submit()
# Wait until list of courses have loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "result--group-start")))
results = driver.find_elements(By.CLASS_NAME, "result--group-start")
# Click on the 4th element of the list
results[4].click()
# Click on the syllabus
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Course Resources')]")))
syllabus_link = driver.find_element(By.LINK_TEXT, "Class Syllabus")
syllabus_link.click()

log_in(driver)

# Download syllabus



WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))

quit()