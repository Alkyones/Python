from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import pandas as pd
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

data = pd.DataFrame(columns=['CompanyName', 'Country', 'MainType', 'DescriptionShort','Description', 'Website', 'Phone', 'Facebook', 'Twitter', 'LinkedIn','Instagram'])
linkData = pd.DataFrame(columns=['link'])
# driver = uc.Chrome(use_subprocess=True)
driver = webdriver.Chrome()

# Create object page

cookies = {
    "personalization_id": "v1_jeRZEA5z5RaIyb4z+BgAbg==",
}

 
companyLinks = []


# get all company links
for i in range(126):
    if i == 0:
        url = 'https://www.europages.co.uk/companies/fruit%20importers.html'
    else:
        url = f"https://www.europages.co.uk/companies/pg-{i+1}/fruit%20importers.html"
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

    companiesListTotal = soup.find_all('ol', class_='ep-page-serp-companies__epages-list')
    for companyList in companiesListTotal:
        lis = companyList.find_all('li', class_='ep-ecard')
        for li in lis:
            a = li.find('a', class_='ep-ecard-serp__epage-link')
            companyLinks.append(a['href'])
            linkData.loc[len(linkData.index)] = a['href']
        print(len(companyLinks))

linkData.to_csv('linkList.csv', index=False)


count = 1
#get company details
for company in companyLinks:
    print(count)
    count += 1
    try:
        url = f'https://www.europages.co.uk{company}'
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        if soup.find('h1', class_='ep-epages-header-title'):
            speciality = soup.find('h1', class_='ep-epages-header-title').text.lower().strip().replace('\n', '')
            speciality = re.sub("\s\s+", " ", speciality)
        else: speciality = ''
        if soup.find('div', class_='v-card__subtitle'):#
            companyName = soup.find('div', class_='v-card__subtitle').text.strip().split('\n')[0]
        companyMainActivity = soup.find('span', class_='ep-main-activity-name').text.strip()

        try:
            l = driver.find_element(By.CLASS_NAME, "ep-epage-sidebar__phone-button")
            driver.execute_script("arguments[0].click();", l);
            time.sleep(1)
            l = driver.find_element(By.CLASS_NAME, "ep-epage-phone-popup-number__button")
            driver.execute_script("arguments[0].click();", l);
            time.sleep(1)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')

            phone = soup.find('span', class_="ep-epage-phone-popup-number__button-text").text
        except:
            phone = 'Not found'

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        website = ''
        if soup.find('a', class_="ep-epage-sidebar__website-button"):
            website = soup.find('a', class_="ep-epage-sidebar__website-button")['href'].strip()

        country = ''
        country = soup.find('div', class_="v-card__subtitle").find('p').text   

        description = ''
        if soup.find('p', class_='ep-text-with-overflow__text'):
            description = soup.find('p', class_='ep-text-with-overflow__text').text

        facebook,twitter,linkedin,instagram = '', '', '', ''

        social_medias = soup.find_all('a', class_="ep-epages-home-links__social-link")
        if social_medias:
            for social in social_medias:
                if 'facebook' in social['href']:
                    facebook = social['href']
                elif 'twitter' in social['href']:
                    twitter = social['href']
                elif 'linkedin' in social['href']:
                    linkedin = social['href']
                elif 'instagram' in social['href']:
                    instagram = social['href']
        print(companyName,speciality)
        print(phone,website)
        print(companyMainActivity)
        print(facebook,twitter,linkedin,instagram)
        data.loc[len(data.index)] =[companyName, country, companyMainActivity, speciality,description, website, phone, facebook, twitter, linkedin, instagram]
        print('---------------------------------------------')
    except:
        print('Not Found')

data.to_csv('europages.csv',index=False)