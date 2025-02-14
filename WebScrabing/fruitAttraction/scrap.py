from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
import time
import os 
import json
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)



data = pd.DataFrame(columns=['CompanyName', 'Stand','Location', 'Mail','Website','Categories', 'Geographic region of operation',"Products and services offered", "Brochure link", "Company's activity", "Coexhibitor of" ])
script_dir = os.path.dirname(__file__)
data_csv_path = os.path.join(script_dir, 'data.csv')
dataLists = pd.read_csv(data_csv_path, usecols =['link', 'email'])
resultLinks = [{'link': row['link'], 'email': row['email']} for index, row in dataLists.iterrows()]
failedLinks = []

for linkData in resultLinks:
    try:
        url = linkData['link']
        driver.get(url)

        time.sleep(3)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        soup = json.loads(soup.find("pre").text)
        companyName = "Not found"
        standNo = "Not found"
        location = "N/A"
        email = linkData['email']
        website = "N/A"
        categories = 'N/A'
        groo = 'N/A'
        paso = 'N/A'
        bl = 'N/A'
        ca = 'N/A'
        coexh = ''
        
        if soup['name']:
            if soup['name'] != '':
                companyName = soup['name']
        if soup['link'] and soup['link'] != '':
            website = soup['link']
        if soup['stands']:
                if len(soup['stands']) > 0:
                    standNo = f'Stand {soup['stands'][0]['name']} - {soup["stands"][0]["location"]}'
        if soup['location']:
            location = f'{soup['location']['address']} / {soup['location']['city']} / {soup['location']['region']} / {soup['location']['countryCode']}'

        if soup['categories'] and len(soup['categories']) > 0:
            categories = ', '.join(soup['categories'])
        if soup['parentName'] and soup['parentName'] != '':
            coexh = soup['parentName']

        groo = ''.join(dynamicValue['value'] for dynamicField in soup['dynamicFields']
                if dynamicField['name'] == "Geographic region of operation"
                for dynamicValue in dynamicField.get('values', []))
        paso = ''.join(dynamicValue['value'] for dynamicField in soup['dynamicFields']
                if dynamicField['name'] == "Products and services offered"
                for dynamicValue in dynamicField.get('values', []))
        bl = ''.join(dynamicValue['value'] for dynamicField in soup['dynamicFields']
                if dynamicField['name'] == "Brochure link"
                for dynamicValue in dynamicField.get('values', []))
        ca = ''.join(dynamicValue['value'] for dynamicField in soup['dynamicFields']
                if dynamicField['name'] == "Company's activity"
                for dynamicValue in dynamicField.get('values', []))
        if groo == '': groo = 'N/A'
        if paso == '': paso = 'N/A'
        if bl == '': bl = 'N/A'
        if ca == '': ca = 'N/A'

        print('-----------------------')
        print(companyName)
        print(standNo)
        print(location)
        print(email)
        print(website)
        print(categories)
        print(coexh)
        print(groo)
        print(paso)
        print(bl)
        print(ca)
        print('------------------------')
        
        data.loc[len(data.index)] = [companyName, standNo,location, email, website, categories, groo, paso, bl, ca, coexh]
    except Exception as e:
        print(e)
        print("Failed to find")
        failedLinks.append(linkData['link'])
    # break
        
data.to_csv("fruitAttraction2023_EN.csv", index=False)
print(failedLinks)