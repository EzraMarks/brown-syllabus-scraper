from turtle import pd
import turtle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service("./chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://cab.brown.edu")

department_dropdown = driver.find_element(By.ID, "crit-dept")
department_selector = Select(department_dropdown)
department_selector.select_by_index(1)

find_courses_form = driver.find_element(By.ID, "search-form")

find_courses_form.submit()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "result--group-start")))

results = driver.find_elements(By.CLASS_NAME, "result--group-start")
results[4].click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Course Resources')]")))

syllabus_link = driver.find_element(By.LINK_TEXT, "Class Syllabus")
syllabus_link.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

# username_field = 
# password_field = 

quit()