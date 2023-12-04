import pandas as pd
import time
import os

from bs4 import BeautifulSoup

# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver

from dotenv import load_dotenv
load_dotenv()

url = 'https://www.linkedin.com'
driver = webdriver.Chrome()
driver.get(url)

def write_file(el):
    job_id = el.get('data-job-id')

    # Open the web page
    driver.get(url + el.find('a').get('href'))
    time.sleep(3)

    html = driver.execute_script("return document.body.outerHTML;") # Javascript script
    soup = BeautifulSoup(html, 'html.parser')

    file_path = f'./data/jobs_html/{job_id}.txt'
    with open(file_path, 'w') as file:
        file.write(str(soup))
    time.sleep(3)

def create_html_files(list_):
    for i in list_:
        write_file(i)

def scrapping():

    time.sleep(2)

    email_box = driver.find_element(By.ID, "session_key")
    password_box = driver.find_element(By.ID, "session_password")

    # 2. Declare variables
    email = os.getenv("email")
    password = os.getenv("password")

    # 3. Send the text
    email_box.send_keys(email)
    password_box.send_keys(password)

    # 4. Hit enter
    password_box.send_keys(Keys.RETURN)

    time.sleep(15)
    # Navigate to jobs tab
    jobs_button = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/nav/ul/li[3]/a')
    jobs_button.click()

    time.sleep(2)
    # Filter for job title
    job_box = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
    time.sleep(1)
    job_box.send_keys('machine learning engineer')
    job_box.send_keys(Keys.ENTER)

    time.sleep(2)
    # Filter for location
    location_box = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
    time.sleep(1)
    location_box.clear()
    time.sleep(3)
    location_box.send_keys('United States')
    location_box.send_keys(Keys.ENTER)

    # Save current link
    current_link = driver.current_url

    # Job scrapping with bs4
    html = driver.execute_script("return document.body.outerHTML;")
    soup = BeautifulSoup(html, 'html.parser')

    pagination = soup.find_all('ul', {'class': 'artdeco-pagination__pages--number'})
    pagination = pagination[0].find_all('button')[:8]

    for btn in pagination:
        for _ in range(5):  # You can adjust the range as needed
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        aria = btn.get("aria-label")
        button = driver.find_element(By.XPATH, f'//button[@aria-label="{aria}"]')
        button.click()

        current_link = driver.current_url
        html = driver.execute_script("return document.body.outerHTML;")
        soup = BeautifulSoup(html, 'html.parser')

        time.sleep(3)
        container = soup.find_all('ul', {'class': 'scaffold-layout__list-container'})
        container = container[0]
        list_ = container.find_all('div', {'class': 'job-card-container'})
        create_html_files(list_)
        driver.get(current_link)
        container = []
        list_ = []
        time.sleep(3)

    driver.quit()