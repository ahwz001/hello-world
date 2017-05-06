# coding:utf-8
# deal_html.py
# add html <head>......</head>

# Merge all the html

import os

def deal_sum_file():
    head = """
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    </head>
    \n
    <body>
    """
    with open("2017-01-01.html", 'w') as fn:
        fn.write(head)
    file_list = os.listdir('.')
    file_list.sort()
    with open("2017-01-01.html", 'a') as fn:
        for i in file_list[1:-1]:
            print i
            t = open(i, 'r')
            content = t.read()
            t.close()
            fn.write(content)
        fn.write('\n</body>')


if __name__ == "__main__":
    deal_sum_file()

