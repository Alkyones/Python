from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
import time
import undetected_chromedriver as uc


data = pd.DataFrame(columns=['CompanyName', 'Categories', 'Address', 'Email', 'Phone', 'Website'])

driver = uc.Chrome(use_subprocess=True)
url = 'https://aiwa.ae/category/fruits-vegetables-importers-wholesalers'
# Create object page
driver.get(url)
cookies = {
    "personalization_id": "v1_jeRZEA5z5RaIyb4z+BgAbg==",
}

 


time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
lists = soup.find_all('ul', class_='searchList')[0].find_all('li')
hrefList = []
for item in lists:
    if item.find('div', class_='centerAlign'):
        link = item.find('a')['href']
        hrefList.append(link)

for href in hrefList:
    url = 'https://aiwa.ae' + href
    driver.get(url)
    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    
    companyName = soup.find('h1', itemprop='name').text.strip()
    print(companyName)
    categories = []
    if soup.find('ul', class_='categoryList'):
        ctgList = soup.find_all('ul', class_='categoryList')[0].find_all('li')
        for category in ctgList:
            cat = category.find('a').contents[0]
            cat = cat.replace('\n', '').strip()
            categories.append(cat)
        
    phone, email, website = '', '', ''
    address = ''
    if soup.find('ul', class_='detailsListing'):
        if soup.find_all('li', itemprop='telephone'):
            phone = soup.find_all('li', itemprop='telephone')[0].find('a').text.strip()
            phone = phone.replace(' ', '')
            phone = phone[0:3] + ' ' + phone[4] + ' ' + phone[5:]
        if soup.find_all('li', itemprop='email'):
            email = soup.find_all('li', itemprop='email')[0].find('a').text.strip()
        if soup.find_all('li', itemprop='url'):
            website = soup.find_all('li', itemprop='url')[0].find('a').text.strip()
        print(phone,email,website)
        if soup.find('span', class_='addressPadding'):
            address = soup.find('span', class_='addressPadding').text.strip()
        print(address)
        print(categories)
        categories = ','.join(categories)
        data.loc[len(data.index)] = [companyName, categories, address, email, phone, website] 
        print('-------------------------------')

data.to_csv("aiwa.csv",index=False)