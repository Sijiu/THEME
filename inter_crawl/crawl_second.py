# -*- coding: utf-8 -*-

import urllib
import urllib2

import os


def getPage(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


url = 'http://www.dataanswer.top/'
result = getPage(url)
file_name = 'test.doc'
file_path = 'doc'
if os.path.exists(file_path) == False:
    os.makedirs(file_path)
local = os.path.join(file_path, file_name)
f = open(local, "w+")
f.write(result)
f.close()


# #coding=utf-8
# import urllib
# import urllib2
# import os
#
#
def getPage(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


url = 'http://www.dataanswer.top/'  # 把该地址改成图片/文件/视频/网页的地址即可
result = getPage(url)
file_name = 'test.doc'
file_path = 'doc'
if os.path.exists(file_path) == False:
    os.makedirs(file_path)
local = os.path.join(file_path, file_name)
urllib.urlretrieve(local)
