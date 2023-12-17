import os, sys
import json
import time

from database import Database
from utils import *

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


#give credentials file path or initialize your database here
#example for credentials file:
# {
#     "dbUrl": "your_db_url",
#     "collectionName":"your_collection_name_if_exists",
#     "dbName": "your_db_name",
# }
credentialFile = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../credentials")
)



def getScrapedDataFromLinks(links, url_base):
    scrapedTopList = {}
    for link in links:
        cleanedItems = []

        driver.get(url_base + link)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "lxml")
        
        selectedCategory = soup.find("a", {"class": "nav-b"})
        # selectedCategoryBackup = soup.find("a", {"class": ""})
        if selectedCategory :
            title = selectedCategory["aria-label"]
            print("title: " + title, " url:", url_base + link)
            items = soup.find_all("div", {"id": "gridItemRoot"})
            for item in items:
                spans = item.find_all("span")
                rank = spans[0].text
                description = spans[1].text
                price = findPrice(item)
                
                link = item.find("a", {"class": "a-link-normal"})
                link = url_base + link["href"]
                
                cleanedData = {
                    'rank': rank,
                    'product': description,
                    'price': price,
                    'link': link
                }
                cleanedItems.append(cleanedData)
            scrapedTopList[title] = cleanedItems
            time.sleep(4)
        else:
            print(selectedCategory)
            print("title is not found for link: ", url_base + link )
                
        print("Getting the data")
    # DB.insertDoc(credentials['collectionName'], scrapedTopList)
    return True


def getCredentials():
    try:
        with open(f"{credentialFile}/amazonPipeline.json", "r") as file:
            creds = json.load(file)
            file.close()
            return {
                "connectionUrl": creds["dbUrl"],
                "collectionName": creds["collectionName"],
                "dbName": creds["dbName"],
            }
    except:
        print("Could not find credential file or credentials.")
        return None


credentials = getCredentials()
if credentials is None:
    sys.exit("No credentials found hence program is closed.")

# DB connection
DB = Database(credentials)

url_base = "https://www.amazon.com"
url = f"{url_base}/Best-Sellers/zgbs"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome()
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "lxml")

containerData = soup.find_all("div", {"class": "a-size-base a-inline-block"})
links = getLinksFromList(containerData)

if not links:
    print("No links found")
    sys.exit()

scrapedData = getScrapedDataFromLinks(links, url_base)


DB.disconnectDb()
