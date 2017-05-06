#coding:utf-8

from lxml import etree

# 定义一个函数，给他一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)

# 下面是我们实战的第一个html
sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""

