from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def eventCrawler():
    options = Options()
    options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    options.add_argument("--headless")

    url = "https://www.eventbrite.com/d/online/all-events/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    newsToSave = []
    listNews = soup.find('div', {'class':'search-results-panel-content'}).find('ul', {"class": "search-main-content__events-list"}).find_all('li')
    for li in listNews:
        newObj = {}
        sectionTitleInfo = li.find('section')
        ps = sectionTitleInfo.find_all("p", {"class": "Typography_align-match-parent__4bejd"})
        print(ps)
        if sectionTitleInfo:
            print(sectionTitleInfo)
            link = sectionTitleInfo.find("a")["href"]
            title = sectionTitleInfo.find("h2").text
            eventDate = ps[0].text
            publisher = "No Publisher"
        
            img = sectionTitleInfo.find('img')
            if img : img = img['src']
            else: img = 'not found'
        
            newObj['link'] = link
            newObj['title'] = title
            newObj['image'] = img
            newObj['timeEvent'] = eventDate
            newObj['publisher'] = publisher
            newsToSave.append(newObj)
        for item in newsToSave:
            # so = SavedEvents.objects.create(**item)
            print(item)
            # so.save()
    return


eventCrawler()