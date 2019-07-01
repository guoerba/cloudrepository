# -*- coding=utf-8 -*-
import requests
import re
from lxml import etree


def xpathfind(url):
    if not type(url) == type(" "):
        print("url应该是字符串!!!!")

        return
    print("good")

if __name__ == '__main__' :
    html = requests.get(url="https://www.jikexueyuan.com/")
    #print = (re.findall("<>"))
    sector = etree.HTML(html.text)
    print(sector.xpath('//div[@class="zhiye"]/h2/text()'))
    for tag in sector.xpath('//a/@href'):
        print(tag)
    #print()