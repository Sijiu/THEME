# -*- coding: utf-8 -*-

#coding=utf-8
import urllib
import urllib2
url = 'http://www.dataanswer.top'
headers = {
	'Host':'www.dataanswer.top',
	'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
	#'Accept':'application/json, text/javascript, */*; q=0.01',
	#'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
	#'Accept-Encoding':'gzip,deflate',
	#'Referer':'http://www.dataanswer.top'
}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
page = response.read()
print page
