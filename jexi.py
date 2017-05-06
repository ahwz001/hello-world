# jiexi
# gupiao

import requests
from bs4 import BeautifulSoup


def getHTML(url):
    # header = {'user-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
    r = requests.get(url)
    print r
    return r.content


def parseHTML(html):
    print 'parseHTML()'
    soup = BeautifulSoup(html,'html.parser')

    body = soup.body
    company_middle = body.find('div',attrs={'class':'middle'})
    company_list_ct = company_middle.find('div',attrs={'class':'list-ct'})      
    # for company_ul in company_list_ct.find_all('ul',attrs={'class':'company-list'}):
    for company_li in company_list_ct.find_all('li'):
        company_url = company_li.a['href']
        company_info = company_li.get_text()
        print company_info,company_url


if __name__ == '__main__':    
    URL = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
    html = getHTML(URL)
    parseHTML(html)
