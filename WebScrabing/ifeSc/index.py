from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


#class
#m-exhibitors-list__items__item__header__title__link

data = pd.DataFrame(columns=["Title", "StandNo",'Categories','Website','SocialMedia',"Country"])

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs')
driver = webdriver.Chrome()

url = "https://www.ife.co.uk/exhibitors"
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

companyList = soup.find('ul', {"class": "m-exhibitors-list__items"})
companyLinks = soup.find_all('a', {"class":"js-librarylink-entry"})



page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')


while soup.find('a', {'class': "pagination__list__item__link pagination__list__item__link--next"}):
    try:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        #scr
        title = 'N/A'
        if(soup.find('h1', {"class": "m-exhibitor-entry__item__header__title"})):
            title = soup.find('h1', {"class": "m-exhibitor-entry__item__header__title"}).text.strip()

        standNo = 'N/A'
        if(soup.find('div', {"class": "m-exhibitor-entry__item__header__stand"})):
            standNo = soup.find('div', {"class": "m-exhibitor-entry__item__header__stand"}).text.strip()
            standNo = standNo.replace('Stand: ', '')

        #m-exhibitor-entry__item__header__categories
        categories = []
        if(soup.find('ul', {"class": "m-exhibitor-entry__item__header__categories"})):
            allItems = soup.find('ul', {"class": "m-exhibitor-entry__item__header__categories"})
            items = allItems.find_all('li')
            for item in items:
                categories.append(item.text.strip())
        categories = sorted(categories)


        #m-exhibitor-entry__item__body__contacts__additional__website  
        website = 'N/A'
        if(soup.find('div', {"class": "m-exhibitor-entry__item__body__contacts__additional__website"})):
            websiteLink = soup.find('div', {"class": "m-exhibitor-entry__item__body__contacts__additional__website"})
            website = websiteLink.find('a').text.strip()

        #m-exhibitor-entry__item__body__contacts__social
        socialMedias = []
        if(soup.find('ul', {"class": "m-exhibitor-entry__item__body__contacts__social"})):
            socialMediaUl = soup.find('ul', {"class": "m-exhibitor-entry__item__body__contacts__social"})
            socialMediaItems = socialMediaUl.find_all('li')
            for item in socialMediaItems: 
                socialMedias.append(item.find('a')['href'])
        socialMedias = sorted(socialMedias)
        country = 'N/A'
        if(soup.find('div', {"class":"m-exhibitor-entry__item__body__contacts__address"})):
            country = soup.find('div', {"class":"m-exhibitor-entry__item__body__contacts__address"}).text
            country = country.replace('Address', '').strip()

        if len(categories) == 0:
            categories = 'N/A'
        if len(socialMedias) == 0:
            socialMedias = 'N/A'

        data.loc[len(data.index)] = [title, standNo, website, categories, socialMedias, country]
        print('--------------------------------------------------------')
        print(title, country)
        print(standNo)
        print(website)
        print(categories)
        print(socialMedias)
        print('--------------------------------------------------------')
        #pagination class="pagination__list__item__link pagination__list__item__link--next
        l = driver.find_element(By.CLASS_NAME, "pagination__list__item__link--next")
        driver.execute_script("arguments[0].click();", l);
        time.sleep(5)
    except:
        print('---------------------NO DATA-----------------------------------')


data.to_csv('ifeData.csv', index=False)
