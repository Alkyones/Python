from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyclip

data = pd.DataFrame(columns=['CompanyName', 'Country', 'Phone', 'Mail','Website','Years', 'StandNo', 'Cat'])

options = webdriver.EdgeOptions()
# options.add_argument('--user-data-dir=C:\\Users\\lifeo\\AppData\\Local\\Microsoft\\Edge\\User Data')
options.add_argument('--incognito')

driver = webdriver.Edge()

url = 'https://online.fruitlogistica.com/showfloor#organization'
driver.get(url)

time.sleep(50)

try:
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new page segment to load
        time.sleep(3)  # Adjust the sleep duration based on your network speed

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        # Add your code here to extract the data from the page
        # e.g., driver.find_elements(By.CSS_SELECTOR, '.item')
except Exception as e:
    print(e)
finally:
    driver.quit()  # Close the browser
    

# ## GET PUBLIC URLS FOR COMPANIES ###
# dataLinks = pd.DataFrame(columns=['Link'])
# with open("index.html", encoding='utf8') as f:
#     soup = BeautifulSoup(f, "lxml")


# links = soup.find_all("a", type='organization')
# for link in links:
#     print('\n')
#     if(link.find("a")):
#         newLink = url + link.find("a").get("href")
#         print(newLink)
#         dataLinks.loc[len(dataLinks.index)] = [newLink]

# dataLinks.to_csv("fruitLogisticaLinks.csv",index=False)


###Use csv file ###
# dataLists = pd.read_csv("C:\\Users\\lifeo\\Desktop\\Python\\fruitLogisticaLinks.csv", usecols =['Link'])

# resultLinks = [x for x in dataLists['Link']]


    

# for link in resultLinks:
#     try:
#         url = link
#         driver.get(url)

#         time.sleep(1)
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'lxml')
#         time.sleep(5)

#         companyName = soup.find("h3").text.strip()
#         dataS = soup.find("div", {"class": "eKOBui"})
#         allP = dataS.find_all('div', {"class": "bjXztA"})

#         country = '-'
#         if(allP[0].find_all('p')[-1].text.strip()):
#             country = allP[0].find_all('p')[-1].text.strip()

#         website,phone,mail = '-','-','-'

#         if(allP[1].find_all('p')):
#             elem = allP[1].find_all('p')
#             if(len(elem) == 1):
#                 website = allP[1].find_all('p')[0].text.strip()
#             if len(elem) == 2:
#                 website = allP[1].find_all('p')[0].text.strip()
#                 phone = allP[1].find_all('p')[1].text.strip()
#             if len(elem) == 3:
#                 website = allP[1].find_all('p')[0].text.strip()
#                 phone = allP[1].find_all('p')[1].text.strip()
#                 mail = allP[1].find_all('p')[2].text.strip()

#         year = []
#         if(soup.find("div", {"class": 'dEGAFB'})):
#             badges = soup.find("div", {"class": 'dEGAFB'})
#             years = badges.find_all("div",{"class":'noIcon'})
#             for i in years:
#                 year.append(i.text.strip())


#         stand = '-'
#         if(soup.find("div", {"class": 'dsIFMs'})):
#             stand = soup.find("div", {"class": 'dsIFMs'}).text.strip()


#         cat = []
#         if(soup.find("div", {"class": 'hTFZFC'})):
#             catsDiv = soup.find("div", {"class": 'hTFZFC'}).find("div",{"class": "llMCnp"})
#             for div in catsDiv:
#                 catInfo = div.text.strip()
#                 if catInfo == 'Branches':
#                     driver.find_element(By.CLASS_NAME, 'sc-gzAkjR').click();
#                     page_source = driver.page_source
#                     soup = BeautifulSoup(page_source, 'lxml')
#                     table = soup.find('ul', {"class": 'rstm-tree-item-group'}).find_all('li')
#                     for c in table:
#                         cat.append(c.text.strip())
        
#     except:
#        print("Failed to find")


#     print('--------------------------------')
#     print(companyName)
#     print(country)
#     print(website,phone,mail)
#     if (len(year) == 0):
#         year = '-'
#     print(year)
#     print(stand)
#     if (len(cat) == 0):
#         cat = '-'
#     print(cat)
        
#     print('----------------------------------')
#     data.loc[len(data.index)]= [companyName, country, phone, mail,website,years, stand, cat]

# data.to_csv("fruitLogistica.csv",index=False)