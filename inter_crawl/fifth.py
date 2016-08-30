# -*- coding: utf-8 -*-

# 利用selenium模拟浏览器，结合html的解析
# coding=utf-8
# 1、安装 python-pip
# sudo apt-get install python-pip
# 2、安装selenium
# sudo pip install -U selenium


from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.newsmth.net/nForum/#!article/Intern/206790')
html = driver.page_source.encode('utf-8', 'ignore') # 这个函数获取页面的html
print(html)
driver.close()
