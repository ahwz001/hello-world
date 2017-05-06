# lunzige

import requests,urllib
from lxml import etree

def get_img(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    r = requests.get(url,headers=headers).text
    s = etree.HTML(r)
    link = s.xpath('//img/@data-original')
    for i in link:
        print(i)
        name = i.split('/')[-1]
        urllib.request.urlretrieve(i,name)


if __name__ == '__main__':
    for i in range(1,15):
        url = 'https://www.zhihu.com/collection/46627456?page=' + str(i)
        get_img(url)

