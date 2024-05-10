from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

url = "https://lc-events-web-public.ifema.es/t/3a88c5e5-a6e1-4898-b72b-103e4eed1731/editions/e9c306af-66f3-4002-1607-08dbe9c30491/exhibitors"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

def find_show_more_button(driver):
    try:
        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollable"]/main/div/div/div[2]/div[2]/button')))
        if elem: 
            return elem
        else:
            return False
    except:
        return False

def click_show_more_button(button):
    #scroll bottom first
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    button.click()
    time.sleep(1)
    return

def get_exhibitors_url(articles):
    exhibitors_url = []
    for article in articles:
        exhibitors_url.append(article.find('a', class_='lc-list-card__title').get('href'))
    return exhibitors_url


try:
    while True:
        button = find_show_more_button(driver)
        if button:
            click_show_more_button(button)
        else:
            print("All cards loaded.")
            break
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    exhibitors_url = get_exhibitors_url(page_source.find_all('article', class_='lc-list-card'))
    print(exhibitors_url)
    df = pd.DataFrame(exhibitors_url)
    
finally:
    driver.quit()