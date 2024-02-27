from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pyclip
data = pd.DataFrame(columns=['CompanyName', 'Country','StandNumber','CompanyInfo', 'Categories','Specialities'])

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def findExhibitorsInPage(driver):
    exhibitors = driver.find_element(By.XPATH,'//*[@id="exhibitors_list_table"]')
    page_source = exhibitors.get_attribute('outerHTML')
    soup = BeautifulSoup(page_source, 'html.parser')
    # print(soup.prettify())
    tableBody = soup.find('tbody')
    findTrElements = tableBody.find_all('tr',)
    
    for trElement in findTrElements:
        companyDetailsDiv = trElement.find('div',{'class':'company-info'})
        scrapCompanyData(companyDetailsDiv)
        time.sleep(1)
    
    return exhibitors


def scrapCompanyData(element):
    companyObj = {
        "Company Name": "",
        "Country:": "",
        "Stand Number:": "",
        "Company Info:": "",
        "Profiles:": "",
        "Categories:": ""
    }
    detailDivs = element.find_all('div')
    for div in detailDivs:
        if div.get('class') != "clear":
            h3 = div.find('h3')
            if(h3 != None):
                companyObj['Company Name'] = h3.text
            h4 = div.find('h4')
            spn = div.find('span')
            if(h4 != None and spn != None):
                companyObj[h4.text] = spn.text
    addToPandas(companyObj)
    return

def addToPandas(companyObject):
    CompanyName = companyObject['Company Name']
    Country = companyObject['Country:']
    StandNumber = companyObject['Stand Number:']
    CompanyInfo = companyObject['Company Info:']
    Categories = companyObject['Profiles:']
    Specialities = companyObject['Categories:']
    prGreen(f'{CompanyName} Added to Pandas.')
    data.loc[len(data.index)]= [CompanyName,Country,StandNumber,CompanyInfo,Categories,Specialities]
    return 


options = webdriver.EdgeOptions()
options.add_argument('--incognito')
driver = webdriver.Edge()
url = 'https://foodafrica-expo.com/exhibitors-list'
driver.get(url)
time.sleep(2)

try:
   
    nextPageButton = driver.find_element(By.XPATH,'//*[@class="next paginate_button"]')
    while(True):
        checkIfDisabled = nextPageButton.get_attribute('class')
        
        exhibitors = findExhibitorsInPage(driver)
        time.sleep(1)
        nextPageButton.click()
        prYellow('Next Page')
        if("paginate_button_disabled" in checkIfDisabled):
            prRed("No more pages")
            break
            
        
        
except Exception as e:
    print('Error Occured')
    prRed(e)
finally:
    driver.quit()  # Close the browser
    data.to_csv("fruitAfrica-2024.csv",index=False)
    prGreen('Data Scraped Successfully and saved to CSV file')
   
