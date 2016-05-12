# -*- coding: utf-8 -*-
__author__ = 'wxy'

import requests
from spider.parser.html_handler import HtmlFile
from spider.lib.utils.code_tools import str2utf8
from spider.lib.nosql.mongo import SpiderCache
from spider.controls.filter_translation import need_translation, valid_url
from urllib2 import quote, unquote
from json import JSONDecoder
import json
import simplejson
import lxml.html.soupparser as soupparser
from spider.lib.nosql.mongo_status import CrawlStatus
import traceback
from datetime import datetime

class Words(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
            "referer": "https://s.taobao.com/",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "accept-encoding": "gzip,deflate",
            "accept-language": "zh-CN,zh;q=0.8",
            "host": "s.taobao.com",
        }
        self.date = str(datetime.now().date()).replace('-', '')
        self.words = []
        self.err_words = []
        self.query_text = ''
        self.url = 'https://s.taobao.com/search'

    def get_common_words(self, query_text):
        self.query_text = quote(query_text)
        self.connect_url(self.url, self.query_text)

    def connect_url(self, url, query_text):
        try:
            data = {'q': query_text, 'js': 1, 'stats_click': 'search_radio_all:1', 'initiative_id': 'staobaoz_20160422', 'ie': 'utf8'}
            req = requests.get(
                url='https://s.taobao.com/search?q={0}&js=1&stats_click=search_radio_all%3A1&initiative_id={1}&ie=utf8'.format(self.query_text, 'staobaoz_'+self.date),
                #data=data,
                headers=self.headers,
                timeout=30,
            )
            #print '``````````````````'
            #print req.text
            self.xml_prase(req.text)
        except Exception:
            try:
                req = requests.get(
                    url=url,
                    headers=self.headers,
                    timeout=30,
                )
                self.xml_prase(req.text)
            except:
                print traceback.format_exc()

    def xml_prase(self, html_doc):
        try:
            root = soupparser.fromstring(html_doc)
            sentence_group = root.xpath('//script')[5].xpath('text()')[0].split(';\n    g_srp_loadCss();')[0].split('g_page_config = ')[1]
            g_page_config = JSONDecoder().decode(sentence_group)

            nav = g_page_config.get('mods').get('nav')
            if nav:
                nav_data = nav.get('data')
                if nav_data.get('common'):
                    for common in nav_data.get('common'):
                        self.words.append(common.get('text'))
                        for word in common.get('sub'):
                            self.words.append(word.get('text'))
                if nav_data.get('adv'):
                    for adv in nav_data.get('adv'):
                        self.words.append(adv.get('text'))
                        for word in adv.get('sub'):
                            self.words.append(word.get('text'))

            sortbar = g_page_config.get('mods').get('sortbar')
            for sortlist in sortbar.get('data').get('sortList'):
                self.words.append(sortlist.get('name'))
                self.words.append(sortlist.get('tip'))

            if sortbar.get('data').get('filter'):
                for filt in sortbar.get('data').get('filter'):
                    self.words.append(filt.get('title'))

            personalbar = g_page_config.get('mods').get('personalbar')
            if personalbar:
                personalbar_data = personalbar.get('data')
                if personalbar_data:
                    if personalbar_data.get('metisData'):
                        for shopitems in personalbar_data.get('metisData').get('shopItems'):
                            self.words.append(shopitems.get('text'))
        except:
            self.err_words.append(self.query_text)
            print traceback.format_exc()

class Taobao(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
            "referer": "https://www.taobao.com/",
            "accept": "*/*",
            "accept-encoding": "gzip,deflate",
            "accept-language": "zh-CN,zh;q=0.8",
            "host": "tce.alicdn.com",
        }
        self.date = str(datetime.now().date()).replace('-', '')
        self.words = []
        self.url = 'https://tce.alicdn.com/api/data.htm?ids=222887%2C222890%2C222889%2C222886%2C222906%2C222898%2C222907%2C222885%2C222895%2C222878%2C222908%2C222879%2C222893%2C222896%2C222918%2C222917%2C222888%2C222902%2C222880%2C222913%2C222910%2C222882%2C222883%2C222921%2C222899%2C222905%2C222881%2C222911%2C222894%2C222920%2C222914%2C222877%2C222919%2C222915%2C222922%2C222884%2C222912%2C222892%2C222900%2C222923%2C222909%2C222897%2C222891%2C222903%2C222901%2C222904%2C222916%2C222924&'

    def connect_url(self):
        try:
            req = requests.get(
                url=self.url+'_ksTS={0}_741&callback=jsonp742'.format(datetime.now().now()),
                headers=self.headers,
                timeout=30,
            )
            print '========'
            self.xml_prase(req.text)
        except Exception:
            try:
                req = requests.get(
                    url=self.url+'_ksTS={0}_741&callback=jsonp742'.format(datetime.now().now()),
                    headers=self.headers,
                    timeout=30,
                )
                self.xml_prase(req.text)
            except:
                print traceback.format_exc()

    def xml_prase(self, html_doc):
        try:
            html_doc = html_doc.split('window.jsonp742&&jsonp742(')[1].split(')')[0]
            g_page_config = JSONDecoder().decode(html_doc)
            for keys in g_page_config:
                for value in g_page_config[keys]['value']['list']:
                    self.words.append(value.get('name'))
        except:
            print traceback.format_exc()


if __name__ == "__main__":
    sp = Words()
    sp.get_common_words("裤子")
    print sp.words
    tb = Taobao()
    tb.connect_url()
    error_w = []
'''
    for word in tb.words:
        try:
            #print word
            #print quote(word)
            sp.get_common_words(word.strip().encode('utf8'))
        except:
            print traceback.format_exc()
            print 'error', word
            error_w.append(word)
    for word in sp.err_words:
        print unquote(word)

    print len(sp.words)
    print sp.words
    print len(tb.words)
    print len(error_w)

    words = list(set(sp.words))
    print len(words)
    fp = open("test.txt", 'a+')
    for word in words:

        fp.write(word.encode("utf8"))
        fp.write('\n')
'''
print type({})
lst = [1, 2, 3, 4]
print lst[0]
