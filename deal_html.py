# coding:utf-8
# deal_html.py
# add html <head>......</head>
# add html <body>......</body>

import os

def deal_html(html):
    head = """
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    </head>
    \n
    """
    body = ["<body>\n","\n</body>"]
    return head + body[0] + html + body[1]


def deal_file():
    file_list = os.listdir('.')
    for i in file_list:
        if i.endswith('.py'):
            continue
        with open(i) as fn:
            t = fn.read()        
        with open(i,'w') as fn:
            fn.write(deal_html(t))
        print i


if __name__ == "__main__":
    deal_file()
