import requests
from bs4 import BeautifulSoup as bs

class Product:
  def __init__(self, name=None, price=None, link=None):
    self.name = name
    self.price = price
    self.link = link


def search_n11(searchKey, productSize):
    r = requests.get(n11 + 'arama?q=' + searchKey, headers=headers)

    if r.status_code != 200:
        return None
    else:
        soup = bs(r.content, 'html.parser')

        if soup.find('div', id="view"):

            productList = [Product() for i in range(productSize)]

            li_list = soup.find('div',id='view').find_all('li', class_='column', limit=productSize)

            for i in range(len(li_list)):
                p = li_list[i].find('div',class_='proDetail')

                if p.find('a', class_='newPrice'):
                    productList[i].price = p.find('a', class_='newPrice').find('ins').get_text(strip=True)
                    productList[i].name = p.find('a', class_='newPrice')['title']
                    productList[i].link = p.find('a', class_='newPrice')['href']
                elif(p.find('a', class_='oldPrice')):
                    productList[i].price = p.find('a', class_='oldPrice').find('del').get_text(strip=True)
                    productList[i].name = p.find('a', class_='oldPrice')['title']
                    productList[i].link = p.find('a', class_='oldPrice')['href']
            
            return productList
    return None
            



def search_hb(searchKey, productSize):
    r = requests.get(hb + 'ara?q=' + searchKey, headers=headers)

    if r.status_code != 200:
        return None
    else:
        soup = bs(r.content, 'html.parser')

        if soup.find(class_="product-list").find('li', class_='search-item').find('a'):

            productList = [Product() for i in range(productSize)]

            li_list = soup.find(class_="product-list").find_all('li', class_='search-item', limit=productSize)

            for i in range(len(li_list)):
                productList[i].link = hb + li_list[i].find('a')['href']
                productList[i].name = li_list[i].find(class_="product-title")['title']

                if li_list[i].find(class_="price-value"):
                    productList[i].price = li_list[i].find(class_="price-value").get_text(strip=True)
                else:
                    productList[i].price = li_list[i].find(class_="price").get_text(strip=True)
            
            return productList
    return None



def search_gg(searchKey, productSize):
    r = requests.get(gg + 'arama/?k=' + searchKey, headers=headers)

    if r.status_code != 200:
        return None
    else:
        soup = bs(r.content, 'html.parser')

        if soup.find(class_="catalog-view"):

            productList = [Product() for i in range(productSize)]

            li_list = soup.find(class_="catalog-view").find_all('li', class_='catalog-seem-cell', limit=productSize)

            for i in range(len(li_list)):
                
                productList[i].link = li_list[i].find('a')['href']
                productList[i].name = li_list[i].find('a')['title']
                productList[i].price = li_list[i].find('p',class_="fiyat").get_text(strip=True)

            return productList
    return None




def search(searchKey, productSize, sites):

    result = []

    productSize = int(productSize)

    if('0' in sites):
        r = search_hb(searchKey, productSize)
        if(r != None):
            result.append(r)
    if('1' in sites):
        r = search_n11(searchKey, productSize)
        if(r != None):
            result.append(r)
    if('2' in sites):
        r = search_gg(searchKey, productSize)
        if(r != None):
            result.append(r)

    # print('\n')

    # if n11_products == None :
    #     print("n11 : None")
    # else:
    #     for p in n11_products:
    #         print("N11\nName:\t{}\nPrice:\t{}\nLink:\t{}\n".format(p.name, p.price, p.link))
    
    return result






n11 = 'https://n11.com/'
hb = 'https://www.hepsiburada.com/'
gg = 'https://www.gittigidiyor.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125'}

