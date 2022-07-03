from time import sleep
import turtle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3

service = Service("./chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://cab.brown.edu")

# Makes CAB stop complaining that you need to narrow down the search options
# Click "Exclude Times" option
exclude_times_checkbox = driver.find_element(By.ID, "crit-custom-meeting-pattern")
exclude_times_checkbox.click()
# Click on first cell to exclude that time
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "select-grid__block")))
sleep(2)
exclude_times_checkbox.send_keys(Keys.TAB)
exclude_times_checkbox.send_keys(Keys.TAB)
exclude_times_checkbox.send_keys(Keys.TAB)
selected_block = driver.find_element(By.CLASS_NAME, "select-grid__block--focus")
selected_block.send_keys(Keys.ENTER)
# Click "Done"
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "meet-pat-btn-search")))
done_button = driver.find_element(By.CLASS_NAME, "meet-pat-btn-search")
done_button.click()
# Click "Find Courses" button to search
# sleep(2)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-button")))
search_button = driver.find_element(By.ID, "search-button")
search_button.click()

# Wait until list of courses have loaded
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "result--group-start")))
results = driver.find_elements(By.CLASS_NAME, "result--group-start")

# Create connection to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "syllabi";')

# Create table in the database and add data to it
c.execute('''
    CREATE TABLE syllabi (
        course_code VARCHAR(255) NOT NULL PRIMARY KEY,
        department VARCHAR(255),
        course_number VARCHAR(255),
        course_title VARCHAR(255),
        syllabus_link VARCHAR(255)
    );
''')
conn.commit()

for result in results:
    course_code = result.find_element(By.TAG_NAME, "a").get_attribute("data-group")[5:]
    [department, course_number] = course_code.split(" ")
    course_title = result.find_element(By.CLASS_NAME, "result__title").text
    syllabus_link = f"https://coursetools.brown.edu/syllabus/{department}:{course_number}:2022-Spring:S01"

    c.execute('INSERT INTO syllabi VALUES (?, ?, ?, ?, ?)',
        (course_code, department, course_number, course_title, syllabus_link))

    print(course_code)

conn.commit()
conn.close()
quit()
