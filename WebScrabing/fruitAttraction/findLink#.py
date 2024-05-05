from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By

data = pd.DataFrame(columns=['CompanyName', 'Country', 'Phone', 'Mail','Website','Years', 'StandNo', 'Cat'])
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=UserPath")
driver = webdriver.Chrome(options=options)

base= "https://liveconnect-events.ifema.es"



## GET PUBLIC URLS FOR COMPANIES ###
dataLinks = pd.DataFrame(columns=['Link'])

driver.get("https://liveconnect-events.ifema.es/t/3a88c5e5-a6e1-4898-b72b-103e4eed1731/editions/72017f4e-c7f3-4194-bbae-08db4572f431/exhibitors")
time.sleep(10)

buttonFind = True

while buttonFind:
    try:
        showButton = driver.find_element(By.CLASS_NAME, "qa-exhibitors-show-more-link")
    except:
        showButton = False
    if showButton:
        showButton.click()
        time.sleep(1)
    else:
        buttonFind = False


#find all li)nks
page_source = BeautifulSoup(driver.page_source, "lxml")
links = page_source.find_all("a", class_="lc-list-card__title")

for link in links:
    link = base +link["href"]
    dataLinks.loc[len(dataLinks.index)] = [link]
    print(link)
    
dataLinks.to_csv("fruitAttractionLinks.csv", index=False)

