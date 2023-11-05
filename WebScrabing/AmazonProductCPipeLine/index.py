import os, sys
import json
from database import Database
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

credentialFile = os.path.abspath(os.path.join(
                                              os.path.dirname(os.path.realpath(__file__)),
                                              '../../credentials')
                                 )
def getLinksFromList(data):
    links = []
    for el in data:
        link = el.find('a')
        if link: links.append(link['href'])
    print(links)
    
def get_credentials():
    try:
        with open(f'{credentialFile}/amazonPipeline.json', 'r') as file:
            creds = json.load(file)
            file.close()
            return {"connectionUrl": creds['dbUrl'], "collectionName": creds['collectionName'], "dbName": creds['dbName']}
    except:
        print('Could not find credential file or credentials.')
        return None


credentials= get_credentials()
if credentials is None: sys.exit("No credentials found hence program is closed.")

#DB connection
DB = Database(credentials)

url= "https://www.amazon.com.tr/gp/bestsellers?ref_=nav_cs_bestsellers"



options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

containerData = soup.find_all('div', {'class': 'a-size-base a-inline-block'})
getLinksFromList(containerData)







DB.disconnectDb()