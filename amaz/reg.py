# -*- coding: utf-8 -*-

import re
from HTMLParser import HTMLParser
import BeautifulSoup



class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.datas = []

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "div" and attrs["id"] == "subtopics":
            if tag == "a":
                if len(attrs) == 0:
                    pass
                else:
                    for (variable, value) in attrs:
                        if variable == "href":
                            self.links.append(value)

    def handle_data(self, data):
        self.datas.append(data)
        print data


if __name__ == "__main__":
    html_code = """ <a href="www.google.com"> google.com</a> <A Href="www.pythonclub.org"> PythonClub </a> <A HREF = "www.sina.com.cn"> Sina </a> """
    html = """
        <div style="margin: 1em; " id="_modules"><div id="subtopics"><ul>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_30601_cont_17781?ie=UTF8&amp;itemID=30601&amp;language=zh_US">错误 15</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_22951_cont_17781?ie=UTF8&amp;itemID=22951&amp;language=zh_US">错误 3015</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200557810_cont_17781?ie=UTF8&amp;itemID=200557810&amp;language=zh_US">错误 4000</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712450_cont_17781?ie=UTF8&amp;itemID=200712450&amp;language=zh_US">5000 系列错误代码</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_201440690_cont_17781?ie=UTF8&amp;itemID=201440690&amp;language=zh_US">8000 系列错误代码</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_31601_cont_17781?ie=UTF8&amp;itemID=31601&amp;language=zh_US">错误 10018</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_24761_cont_17781?ie=UTF8&amp;itemID=24761&amp;language=zh_US">错误 11003</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712510_cont_17781?ie=UTF8&amp;itemID=200712510&amp;language=zh_US">13000 系列错误代码</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712520_cont_17781?ie=UTF8&amp;itemID=200712520&amp;language=zh_US">18000 系列错误代码</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712530_cont_17781?ie=UTF8&amp;itemID=200712530&amp;language=zh_US">20000 系列错误代码</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712500_cont_17781?ie=UTF8&amp;itemID=200712500&amp;language=zh_US">30000 系列错误代码</a></li>
        <li><a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712050_cont_17781?ie=UTF8&amp;itemID=200712050&amp;language=zh_US">90000 系列错误代码</a></li>
        </ul>
    """
    hp = MyHTMLParser()
    # hp.feed(html)
    # hp.close()
    # print(hp.links)
    # print(hp.datas)
    # SERIA = re.compile(r'https')
    # result1 = re.match(SERIA, hh)
    # print "result==", result1.group()
