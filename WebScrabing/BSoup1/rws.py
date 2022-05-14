from bs4 import BeautifulSoup
import requests


# def get_soup_price(url,classO):
#     result = requests.get(url)
#     #print(result.text)
#     soup = BeautifulSoup(result.text, 'html.parser')
#     current_price = soup.find(class_=classO)
#     print (current_price.text)



# get_soup_price('https://www.newegg.com/p/N82E16824475024?Item=N82E16824475024&cm_sp=Dailydeal_SS-_-24-475-024-_-05132022','price-current')
# get_soup_price('https://www.ciceksepeti.com/xiaomi-mi-11-lite-uyumlu-yeni-nesil-sik-tasarimli-kullanisli-pembe-watch-6-series-akilli-saat-kcm45737347?gclid=Cj0KCQjwg_iTBhDrARIsAD3Ib5jXGQhfpfFl_qraQUT4JqUsBfVvbWLSBAcecPX6MbLfY5dEKlBRNcAaAirdEALw_wcB',"product__info__new-price__integer js-price-integer")




def get_soup_currency(url,ars):
    result = requests.get(url)
    print(result.text)
    soup = BeautifulSoup(result.text, 'html.parser')
    current_price = soup.find_all('div', class_='overviewRow__66339412a5')
    print (current_price)


get_soup_currency("https://www.bloomberg.com/quote/USDTRY:CUR",'result')