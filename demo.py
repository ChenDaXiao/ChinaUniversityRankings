# #!/usr/bin/python
# -- coding: utf-8 --
# @Time : 2020/4/7 0002 下午 17:51
# @Author : 陈大笑
# @File : demo.py
# @Software: PyCharm
# @Function : 中国大学排名定向爬虫

"""
    功能描述
        输入：大学排名URL链接
        输出：大学排名信息的屏幕输出（排名，大学名称，总分）
        技术路线：requests-bs4
        定向爬虫：仅对输入URL进线爬取，不扩张爬取
    程序的结构设计
        步骤1：从网络上获取大学排名网页内容
        步骤2：提取网页中信息到合适的数据结构
        步骤3：利用数据结构展现并输出结果
"""

import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    """
        从网络上获取大学排名网页内容
    """
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    """
        提取网页中信息到合适的数据结构
    """
    soup = BeautifulSoup(html, "html.parser")
    # 变量查找tbody孩子tr的内容（每一个tr对应着每一条大学名字排名信息等）
    for tr in soup.find('tbody').children:
        # 判断tr的类型
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # 添加td的内容
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    """
        利用数据结构展现并输出结果
    """
    # 解决中文对齐问题的解决（采用中文字符的空格填充chr(12288)）
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    # 打印表头
    print(tplt.format("排名", "学校名称", "省市", "总分", chr(12288)))
    # 需要打印到排名第几的学校
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


def main():
    uinfo = []
    # url链接
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # 打印大学信息,20 univs
    printUnivList(uinfo, 20)


main()

