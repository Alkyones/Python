from bs4 import BeautifulSoup
import requests

with open('WebScrabing\BSoup1\index.html','r') as f:
    soup = BeautifulSoup(f, 'html.parser')


#print(soup.prettify())
# #find 
# Titletag = soup.find('title')
# print(Titletag.text)

# Titletags = soup.find_all('title')
# print(Titletags[1].text)
#findall
# tags = soup.find_all('p') # bulunanlardan liste cikarir
# tag = tags[0] # o listeden istenilen elemani cikarir
# print(tag.find('i').text) # i nin textini cikarir
#print(tag.find_all('b'))

# find_h3 = soup.find('h3' , class_= 'class1')

# print(soup.prettify())








## with real world solution

# url = 'https://www.newegg.com/p/N82E16824475024?Item=N82E16824475024&cm_sp=Dailydeal_SS-_-24-475-024-_-05132022'
# result = requests.get(url)

# #print(result.text)
# soup = BeautifulSoup(result.text, 'html.parser')

# #find the price
# # prices = soup.find_all(text='$')
# # print(prices[1].parent.find('strong').text)


# current_price = soup.find(class_='price-current')
# print(current_price.text)
# parent = prices[0].parent
# print(parent.text)
# strong = parent.find('strong')
# print(strong.text)