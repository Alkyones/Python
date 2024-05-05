from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time


options = webdriver.ChromeOptions()
options.add_argument("user_path")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(
    f"https://www.ebay.com/sch/i.html?_nkw=Top%20Books&norover=1&mkevt=1&mkrid=711-156598-758071-3&mkcid=2&mkscid=102&keyword=top%20books&crlp=436325962545_&MT_ID=585516&geo_id=10232&rlsatarget=kwd-294772395580&adpos=&device=c&mktype=&loc=21070&poi=&abcId=1141746&cmpgn=6616582754&sitelnk=&adgroupid=82636309407&network=g&matchtype=p&gclid=Cj0KCQjwn_OlBhDhARIsAG2y6zNaorN8k6mjPaPWFF8ugxd9nAywehbG-Rq3Nw3SlSiZFMWfp9WBDEMaAgMQEALw_wcB"
)

page_source = BeautifulSoup(driver.page_source, "lxml")


data = ''
cardContainer = page_source.find("ul", {"class": "srp-list"})

print(cardContainer.get_text())
for card in cardContainer:
    data += str(card)
    



   
with open('data.txt', "w", encoding="utf-8") as file:
    
    file.write(data)
    file.close()
