# coding:utf-8
# chuansong.me
# lianyue

import time
import random
import requests
from bs4 import BeautifulSoup
from lxml import etree


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def parse_url_to_html(name,url):
    global header
    response = requests.get(url,headers=header)
    soup = BeautifulSoup(response.content,'html5lib')
    # body = soup.find_all(attrs={"class":"rich_media "})[0]
    try:
        body = soup.find_all(attrs={"class":"rich_media "})[0]
    except IndexError:
        body = soup.find_all(attrs={"class":"rich_media"})[0]
        # body = soup.find_all(id="essay-body")    
    # else: 
    #     body = soup.find_all(id="essay-body")[0]
    #     body = soup.find_all(id="page-content")[0] 

    html = str(body).encode()    
    with open(name, 'wb') as f:
        f.write(html)
    print(name)


def get_xpath(url):
    return etree.HTML(url)

def get_url():
    global header    
    start_url = "http://chuansong.me/account/ilianyue?start="
    page_list = [start_url + str(i) for i in range(504,588,12)]
    # print(page_list)
    for url in page_list:
        r = requests.get(url,headers=header).content
        get_artical_url(r)
        # time.sleep(random.randint(1,4))    


def get_artical_url(r):
    article_list = []
    name_list = []
    t = get_xpath(r)
    m = t.xpath('//div/h2/span/a/@href')
    for j in m:
        article_list.append('http://chuansong.me' + j)
    n = t.xpath('//div/h2/span/a/text()')
    d = t.xpath('//div/h2/span/span/text()')
          
    for i in range(len(n)):
        temp = d[i] + ' ' + n[i].strip() + '.html'
        name_list.append(temp)
    for i in range(len(article_list)):   
        # print(name_list[i])  
        print(article_list[i])
        time.sleep(random.randint(1,5))
        parse_url_to_html(name_list[i], article_list[i])   


if __name__ == "__main__":
    get_url()


# url = "http://chuansong.me/n/1710360422506"    

# parse_url_to_html(url)