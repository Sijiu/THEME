# -*- coding: utf-8 -*-
#把缩写的站内网址还原
#coding=utf-8
"""
爬取同一个网站所有的url,不包括外链
"""
import urllib2
import re
from bs4 import BeautifulSoup
import time

t=time.time()

HOST=''
CHECKED_URL=[]
CHECKING_URL=[]
RESULT=[]
RETRY=3
TIMEOUT=20

class url_node:
	def __init__(self,url):
		"""
		url节点初始化
		：param url:String 当前url
		"""
		self.url=self.handle_url(url,is_next_url=False)
		self.next_url=[]
		self.content=''


	def handle_url(self,url,is_next_url=True):
		"""
		将所有的url处理成标准形式
		"""
		global CHECKED_URL
		global CHECKING_URL

		#去掉尾部的‘/’
		url=url[0:len(url)-1] if url.endswith('/') else url

		if url.find(HOST)==-1:
			if not url.startswith('http'):
				url='http://'+HOST+url if url.startswith('/') else 'http://'+HOST+'/'+url
			else:
				#如果含有http说明是外链，url的host不是当前的host，返回空
				return
		else:
			if not url.startswith('http'):
				url='http://'+url


		if is_next_url:
			#下一层url放入待检测列表
			if url not in CHECKING_URL:
				CHECKING_URL.append(url)
		else:
			#对于当前需要检测的url将参数都替换为1，然后加入规则表
			#参数相同类型不同的url只检测一次
			rule=re.compile(r'=.*?\&|=.*?$')
			result=re.sub(rule,'=1&',url)
			if result in CHECKED_URL:
				return '[!] Url has checked!'
			else:
				CHECKED_URL.append(result)
				RESULT.append(url)
		return url


	def __is_connectable(self):
		print("进入__is_connectable()函数")
		#检验是否可以连接
		retry=3
		timeout=2
		for i in range(RETRY):
			try:
				#print("进入_..............函数")
				response=urllib2.urlopen(self.url,timeout=TIMEOUT)
				return True

			except:
				if i==retry-1:
					return False


	def get_next(self):
		#获取当前所有的url
		#print("进入get_next()函数")
		soup=BeautifulSoup(self.content)
		next_urls=soup.findAll('a')
		if len(next_urls)!=0:
			for link in next_urls:
				self.handle_url(link.get('href'))
				#print(link.text)



	def run(self):
		#print("进入run()函数")
		if self.url:
			#print self.url
			if self.__is_connectable():
				try:
					self.content=urllib2.urlopen(self.url,timeout=TIMEOUT).read()
					self.get_next()


				except:
					print('[!]Connect Failed')
#处理https开头的url的类和方法
class Poc:
	def run(self,url):
		global HOST
		global CHECKING_URL
		url=check_url(url)


		if not url.find('https'):
			HOST=url[:8]
		else:
			HOST=url[7:]


		for url in CHECKING_URL:
			print(url)
			url_node(url).run()


def check_url(url):
	url='http://'+url if not url.startswith('http') else url
	url=url[0:len(url)-1] if url.endswith('/') else url


	for i in range(RETRY):
		try:
			response=urllib2.urlopen(url,timeout=TIMEOUT)
			return url
		except:
			raise Exception("Connect error")


if __name__=='__main__':
	HOST='www.dataanswer.com'
	CHECKING_URL.append('http://www.dataanswer.com/')
	f=open('36大数据','w')
	for url in CHECKING_URL:
		f.write(url+'\n')
		print(url)
		url_node(url).run()
	print RESULT
	print "URL num:"+str(len(RESULT))
	print("time:%d s") % (time.time()-t)