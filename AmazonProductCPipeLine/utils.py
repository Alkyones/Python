def findPrice(item):
    if(item.find("span", {"class": "a-color-price"})):
        price = item.find("span", {"class": "a-color-price"}).text
        return price
    
    if(item.find("span", {"class": "a-size-base"})):
        price = item.select('span[class*="sc-price"]')[0].text
        return price
    
    return None


def getLinksFromList(data):
    links = []
    for el in data:
        link = el.find("a")
        if link:
            links.append(link["href"])
    return links or False
