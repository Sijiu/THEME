# -*- coding: utf-8 -*-

#广度优先，模拟爬取队列
#coding=utf-8
"""
全网爬取所有链接，包括外链--广度优先
"""
import urllib2
import re
from bs4 import BeautifulSoup
import time


#爬虫开始的时间
t = time.time()
# 设置的暂停爬取条数
N_STOP = 10


# 存放已经爬取过的url
CHECKED_URL = []
# 存放待爬取的url
CHECKING_URL=[]
# 存放连接失败的url
FAIL_URL = []
# 存放不能连接的url
ERROR_URL = []
# 失败后允许连接的次数
RETRY = 3
# 连接超时时间
TIMEOUT = 20


class url_node:
    def __init__(self, url):
        """
        url节点初始化
        ：param url:String 当前url
        """
        self.url = url
        self.conten = ''

    def __is_connectable(self):
        """
        检验url是否可以连接
        """
        # 在允许连接次数下连接
        for i in range(RETRY):
            try:
                # 打开url没有报错，则表示可连接
                response = urllib2.urlopen(self.url, timeout=TIMEOUT)
                return True
            except:
                # 如果在尝试允许连接次数下报错，则不可连接
                if i == RETRY-1:
                        return False

    def get_next(self):
        """
        获取爬取该页中包含的其他所有的url
        """
        soup = BeautifulSoup(self.content)
        # ******************在此处可以从网页中解析你想要的内容************************************
        next_urls = soup.findAll('a')
        if len(next_urls) != 0:
            for link in next_urls:
                tmp_url = link.get('href')
                # 如果url不在爬取过的列表中也不在待爬取列表中则把其放到待爬列表中（没有确保该url有效）
                if tmp_url not in CHECKED_URL and tmp_url not in CHECKING_URL:
                    CHECKING_URL.append(tmp_url)

    def run(self):
        if self.url:
            if self.__is_connectable():
                try:
                    # 获取爬取页面的所有内容
                    self.content = urllib2.urlopen(self.url, timeout=TIMEOUT).read()
                    # 从该页面中获取url
                    self.get_next()
                except:
                    # 把连接失败的存放起来
                    FAIL_URL.append(self.url)
                    print('[!]Connect Failed')
            else:
                # 把不能连接的存放起来
                ERROR_URL.append(self.url)
        else:
            print("所给的初始url有问题！")


if __name__ == '__main__':
    # 把初始的url放到待爬的列表中
    CHECKING_URL.append('http://www.36dsj.com/')
    # 不断的从待爬的列表中获取url进行爬取
    ff = open("Mytest.txt", 'w+')
    i = 0
    for url in CHECKING_URL:
        # 对该url进行爬取
        url_node(url).run()
        # 存放已经爬取过的url
        CHECKED_URL.append(url)
        # 删除CHECKING_URL中已经爬取过的url
        CHECKING_URL.remove(url)
        i += 1
        if i == N_STOP:
            # 打出停止时的url，下次可以把该url作为初始继续
            print url
            print"爬取过的列表长度：%d" % len(CHECKED_URL)
            print"待爬取的列表长度：%d" % len(CHECKING_URL)
            print"连接失败的列表长度：%d" % len(FAIL_URL)
            print"不能连接的列表长度：%d" % len(ERROR_URL)
            break
    ff.write(CHECKED_URL)
    ff.write(CHECKING_URL)
    ff.close()
    print "time:%d s" % (time.time()-t)
