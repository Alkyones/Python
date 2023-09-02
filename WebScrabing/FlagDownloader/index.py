from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import urllib

# options = webdriver.ChromeOptions()
# options.add_argument("--user-data-dir=C:\\Users\\lifeo\\AppData\\Local\\Google\\Chrome")
# options.add_argument("--headless")
driver = webdriver.Edge()

driver.get(
    f"https://www.worldometers.info/geography/flags-of-the-world/"
)


page_source = BeautifulSoup(driver.page_source, "lxml")


media = []
media_elements_container = driver.find_element(By.XPATH, "//div[@style='width:95%; text-align:left']")
media_elements = media_elements_container.find_elements(By.XPATH, "//div[@class='col-md-4']")

for row in media_elements:
    #link
    print(row)
    src = row.find_element(By.XPATH, ".//a")
    src = src.get_attribute("href")
    #name
    name = row.find_element(By.XPATH, ".//div[@style='font-weight:bold; padding-top:10px']")
    name = name.text
    
    print(name)
    print(src)
    
    if src == None: continue
    if src.endswith(".gif"):
        media.append({'name':name,'src':src})

print("Total Number of GIFs Stored is", len(media))

for i in range(len(media)):
    print(media[i])
    element= media[i]['name'].lower()
    element= element.replace(' ','_')
    urllib.request.urlretrieve(str(media[i]['src']),f"frupro/flags/{element}.gif")