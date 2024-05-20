from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

main_url = "https://lc-events-web-public.ifema.es"
url = "https://lc-events-web-public.ifema.es/t/3a88c5e5-a6e1-4898-b72b-103e4eed1731/editions/e9c306af-66f3-4002-1607-08dbe9c30491/exhibitors"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()

def find_show_more_button(driver):
    try:
        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollable"]/main/div/div/div[2]/div[2]/button')))
        if elem: 
            return elem
        else:
            return False
    except:
        return False

def click_show_more_button(button):
    #scroll bottom first
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    button.click()
    time.sleep(1)
    return

def get_exhibitors_url(articles):
    exhibitors_url = []
    for article in articles:
        exhibitors_url.append(article.find('a', class_='lc-list-card__title').get('href'))
    return exhibitors_url

def scrape_exhibitor_url(driver, url):
    time.sleep(3)
    try:     
        title = driver.find_element(By.XPATH, '//*[@id="exhibitor-detail__title"]').text
    except:
        title = 'No Title'
    try:
        article = driver.find_element(By.CLASS_NAME, 'exhibitor-detail__article').find_element(By.CLASS_NAME, 'mb-4').text
    except:
        article = 'No description'
    
    try:
        stand = driver.find_element(By.CLASS_NAME, 'lc-tag').text
    except:
        stand = 'No stand info'
    
    products = []
    try:
        if driver.find_element(By.CLASS_NAME, 'show-dynamics__large-fields'):    
            productsDiv = driver.find_element(By.CLASS_NAME, 'show-dynamics__large-fields')
            productsDiv = productsDiv.find_element(By.CLASS_NAME, 'd-flex').find_elements(By.CLASS_NAME, 'field__dynamic-field-content--bordered')
            if(len(productsDiv) > 0):
                for product in productsDiv:
                    products.append(product.text)
            else:
                products.append("No products")
        else:
            products.append("No products")
    except:
        products.append("No products")
    
    try:
        website = driver.find_element(By.CLASS_NAME, 'lc-link').text
    except:
        website = "No website"
    
    print('-----------------------------')    
    print(title), print(stand)
    print(article)
    print(', '.join(products) )
    print(website)
    print('-----------------------------')
    return {
        'exhibitor_name': title,
        'exhibitor_stand': stand,
        'exhibitor_url': url,
        'exhibitor_description': article,
        'products': ', '.join(products),
        'exhibitor_website': website
    }




try:
    # while True:
    #     button = find_show_more_button(driver)
    #     if button:
    #         click_show_more_button(button)
    #     else:
    #         print("All cards loaded.")
    #         break
    # page_source = BeautifulSoup(driver.page_source, 'html.parser')
    # exhibitors_url = get_exhibitors_url(page_source.find_all('article', class_='lc-list-card'))
    # df = pd.DataFrame(exhibitors_url)
    # df.to_csv('exhibitors_url.csv', index=False)
    csv_file = 'exhibitors_url.csv'
    df = pd.read_csv(csv_file)
    exhibitors_url = df['0'].tolist()
    exhibitors_data = pd.DataFrame(columns=['exhibitor_name','exhibitor_stand', 'exhibitor_url', 'exhibitor_description', 'products', 'exhibitor_website'])
    for url in exhibitors_url:
        exhibitor_url = main_url + url
        driver.get(str(exhibitor_url))
        time.sleep(4)
        exhibitor_data = scrape_exhibitor_url(driver,exhibitor_url)
        exhibitors_data.loc[len(exhibitors_data.index)] = exhibitor_data
        time.sleep(4)

    exhibitors_data.to_csv('exhibitors_data.csv', index=False)


except Exception as e:
    print(e)
finally:
    driver.quit()

