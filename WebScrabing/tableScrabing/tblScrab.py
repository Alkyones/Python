from bs4 import BeautifulSoup
import requests
import pandas as pd


url = arg # crawler pass for url from list
# Create object page
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

tableBody = soup.find("table", id="exhibitors_list_table")
tableElements = tableBody.find("tbody").find_all("tr")

headers = []

for i in tableBody.find_all("th"): 
    title= i.text 
    headers.append(title)

headers = [x for x in headers if x != ""] + ["CompanyInfo","Profile","Categories"]
data = pd.DataFrame(columns = headers)
for tr in tableElements:
    tds = tr.find_all("td")
    companyName = tds[0].find("span").text
    country = tds[1].text
    standNumber = tds[-1].text
    companyInfo,profile,categories= '','',''

    if tds[0].select_one(".company-info"):
        cInfo = tds[0].select_one(".company-info")
        for div in cInfo.find_all("div"):
            if div.find("h4"):
                if div.find("h4").text == "Company Info:":
                    companyInfo = div.find_all("span")[0].text
                
                if div.find("h4").text == "Profiles:":
                    profile = div.find_all("span")[0].text
                    
                
                if div.find("h4").text == "Categories:":
                    categories = div.find_all("span")[0].text
                 
    data.loc[len(data.index)] = [companyName, country, standNumber, companyInfo, profile, categories] 

        
        

print(data)
data.to_csv("foodafrica.csv",index=False)
