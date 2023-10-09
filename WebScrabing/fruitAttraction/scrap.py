from bs4 import BeautifulSoup
import requests
import pyperclip
from selenium import webdriver
import pandas as pd
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from unidecode import unidecode

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\lifeo\\AppData\\Local\\Google\\Chrome")
driver = webdriver.Chrome(options=options)

base= "https://liveconnect-events.ifema.es"



dataLists = pd.read_csv("C:\\Users\\lifeo\\Desktop\\Python\\fruitAttractionLinks.csv", usecols =['Link'])

data = pd.DataFrame(columns=['CompanyName', 'Stand', 'Mail','Website','Location', 'Categories',"Activities", "Services", "Interests"])
resultLinks = [x for x in dataLists['Link']]
failedLinks = []

for link in resultLinks:
    try:
        url = link
        driver.get(url)

        time.sleep(2)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        time.sleep(2)
        
        companyName = ""
        standNo = "Not found"
        categories = []
        location = ""
        email = ""
        if (soup.find("h1", {"id": "exhibitor-detail__title"})):
            companyName = soup.find("h1", {"id": "exhibitor-detail__title"}).text
        
        if(soup.find("div", {"class": "exhibitor-detail__stands"})):
            div = soup.find("div", {"class": "exhibitor-detail__stands"})
            standNo = div.find("span").text
            standNo = standNo.replace("ó", "o")
        
        if(soup.find_all("span", {"class": "lc-tag"})):
            tags = soup.find_all("span", {"class": "lc-tag"})
            tags.pop(0)
            for tag in tags:
                categories.append(tag.text)
            if categories:
                categories = ",".join(categories)
            else:
                categories = ""
        if(soup.find("div", {"class": "location"})):
            divloc = soup.find("div", {"class": "location"})
            location = divloc.find("div").get_text()  
        
        if(soup.find("button", {"title": "Email"})):
            element = driver.find_element(By.CSS_SELECTOR, 'button[type="button"][title="Email"].btn.btn-link.text-dark.px-1.py-0')
            element.click()
            email = pyperclip.paste()
        
        website = ""
       
        try:
            website = driver.find_element(By.CSS_SELECTOR, 'a[target="_blank"][rel="noopener noreferrer"].lc-link.text-break')
            website = website.get_attribute("href")
        
        except:
            website = ""
        
        
        activities, services, interests = [], [], [],     
        if (soup.find("div", {"class": "show-dynamics"})):
            dynamicDiv = soup.find("div", {"class": "show-dynamics"})
            allDynamics = dynamicDiv.find_all("div", {"class": "show-dynamics__field"})
            
            for div in allDynamics:
                title = div.find("p", {"class": "show-dynamics__title"}).text
                
                if title == "Actividad de su empresa":
                    activitiesDiv = div.find("div", {"class": "gap-2"})
                    activitiestext = activitiesDiv.find_all("p", {"class": "lc-tag"})
                    for text in activitiestext:
                        activities.append(text.text)
                    if activities:
                        activities = ",".join(activities)
                        activities = unidecode(activities)
                    
                if title == "Productos y servicios que ofrece":
                    servicesDiv = div.find("div", {"class": "gap-2"})
                    servicestext = servicesDiv.find_all("p", {"class": "lc-tag"})
                    for text in servicestext:
                        services.append(text.text)
                    if services:
                        services = ",".join(services)
                        services = unidecode(services)
                if title == "Principales sectores de interés":
                    interestsDiv = div.find("div", {"class": "gap-2"})
                    intereststext = interestsDiv.find_all("p", {"class": "lc-tag"})
                    for text in intereststext:
                        interests.append(text.text)
                    if interests:
                        interests = ",".join(interests)
                        interests = unidecode(interests) 
        print(companyName, standNo, categories, location, email, website)
        
        if not activities:
            activities = ""
        if not services:
            services = ""
        if not interests:
            interests = ""
        print(activities, services, interests)
        
        data.loc[len(data.index)] = [companyName, standNo, email, website, location, categories, activities, services, interests]
    except Exception as e:
        print(e)
        print("Failed to find")
        failedLinks.append(link)
    
        
data.to_csv("fruitAttraction2023.csv", index=False)
print(failedLinks)