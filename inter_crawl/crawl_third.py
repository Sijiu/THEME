# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'name': 'dataanswer',
    'pwd': 'mxh19921992'
})
# 登录的URL
loginUrl = 'http://www.dataanswer.top/LoginService?action=tologin'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址
gradeUrl = 'http://www.dataanswer.top/LoginService?action=myHome'
# 请求访问
result = opener.open(gradeUrl)
print result.read()
