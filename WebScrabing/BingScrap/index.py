from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
keyword = "when+turkey+established"
# options = webdriver.ChromeOptions() 
# options.add_argument('--user-data-dir=C:\\Users\\lifeo\\AppData\\Local\\Google\\Chrome')
# # options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

# driver.get(f'https://www.bing.com/search?q={keyword}&count=50')
# myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'b_results')))
# print("page ready")
# all_li = BeautifulSoup(driver.page_source, 'lxml')
# all_li = all_li.find("ol", {"id":"b_results"})
# all_li = all_li.find_all("li", {"class":"b_algo"})
# links = ""
# count = 0
# for li in all_li:
#     titleDiv = li.find("h2")
#     # time.sleep(2044)
#     a = titleDiv.find("a")
#     a = a['href']
#     title = titleDiv.text
#     print(title)
    
#     item = str(title) +  " ### " + str(a)

#     links += f"{item}\n"

options = webdriver.ChromeOptions() 
options.add_argument('--user-data-dir=C:\\Users\\lifeo\\AppData\\Local\\Google\\Chrome')
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(f'https://www.bing.com/search?q={keyword}&count=50')
myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'b_results')))
print("page ready")
all_li = BeautifulSoup(driver.page_source, 'lxml')
all_li = all_li.find("ol", {"id":"b_results"})
all_li = all_li.find_all("li", {"class":"b_algo"})
links = ""
count = 0
for li in all_li:
    titleDiv = li.find("h2")
    # time.sleep(2044)
    a = titleDiv.find("a")
    a = a['href']
    title = titleDiv.text
    print(title)
    
    item = str(title) +  " ### " + str(a)

    links += f"{item}\n"