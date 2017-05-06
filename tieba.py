# coding:utf-8

import urllib.request
import requests
from lxml import etree
import os

#url = 'http://tieba.baidu.com/p/2166231880'
url = 'http://tieba.baidu.com/p/1165861759'


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

r = requests.get(url,headers=header).content
print(r)
s = etree.HTML(r)
print(s.xpath('//img/@src'))

count = 0
file_list = os.listdir('.')
print(file_list)

for i in s.xpath('//img/@src'):

    print('\n',count)
    name = i.split('/')[-1]  # 图片名称
    if name in file_list:
        continue
    name = str(count)
    urllib.request.urlretrieve(i, name)
#    urllib.request.urlretrieve(i, name)

    count += 1
    print(count)


print(len(s.xpath('//div/img/@src')))