# -*- coding: utf-8 -*-

import urllib
import urllib2
import zlib
import re
import socket

import datetime
from bs4 import BeautifulSoup
from furion.lib.model.amazon_err import Amazon_err
from furion.lib.model.session import sessionCM
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Amazon_errmsg(object):

    def __init__(self):
        self.postdata = urllib.urlencode({
            "widgetToken": "X2VuY29kaW5nPVVURjgmbGFuZ3VhZ2U9emhfQ04mb3BlbmlkLmFzc29jX2hhbmRsZT1zY19uYV9hbWF6b24mb3BlbmlkLmNsYWltZWRfaWQ9aHR0cCUzQSUyRiUyRnNwZWNzLm9wZW5pZC5uZXQlMkZhdXRoJTJGMi4wJTJGaWRlbnRpZmllcl9zZWxlY3Qmb3BlbmlkLmlkZW50aXR5PWh0dHAlM0ElMkYlMkZzcGVjcy5vcGVuaWQubmV0JTJGYXV0aCUyRjIuMCUyRmlkZW50aWZpZXJfc2VsZWN0Jm9wZW5pZC5tb2RlPWNoZWNraWRfc2V0dXAmb3BlbmlkLm5zPWh0dHAlM0ElMkYlMkZzcGVjcy5vcGVuaWQubmV0JTJGYXV0aCUyRjIuMCZvcGVuaWQubnMucGFwZT1odHRwJTNBJTJGJTJGc3BlY3Mub3BlbmlkLm5ldCUyRmV4dGVuc2lvbnMlMkZwYXBlJTJGMS4wJm9wZW5pZC5wYXBlLm1heF9hdXRoX2FnZT0wJm9wZW5pZC5yZXR1cm5fdG89aHR0cHMlM0ElMkYlMkZzZWxsZXJjZW50cmFsLmFtYXpvbi5jb20lMkZncCUyRmhlbHAlMkZoZWxwLmh0bWwlM0ZpZSUzRFVURjglMjZpdGVtSUQlM0QxNzc4MSUyNmxhbmd1YWdlJTNEemhfVVMlMjZyZWZfJTNEYWdfMTc3ODFfYnJlZF8zMDYwMSZwYWdlSWQ9c2NfbmFfYW1hem9uJnNob3dSbXJNZT0w:cGxwbE14MEVhUnlDVENweTNueEpPZXhkbUtmMEwwT2tKRnRjcUlWK3kyWT06MQ==",
            "rememberMe": "false",
            "username": "yangguoli@actneed.com",
            "password": "yaya2015",
            "sign-in-button": "",
            "metadata1": "OIwpGZoo1E6M203NKSfmoeknjsR5d33e1TzgHq9YfV8oCZ/XgZ0GADuoIvfUjtGapQ03NvqgxlUIDuwxZ8tqpxWtcB7eJDtxUzH46QppFCI4m3htBg80dZhVTkI7z3T5ksk+lLVOkaFstk3iIgzj0uwFoEU9x0Q9JOHvKu4u1c2pdDMtOEJOwQb0e6x/H9/jogqp5jP574i2RTpfLy9V6WnU9x1rexfE4k1g35Gpkmcr1alxTDKq2SgyyYGTgaghxusEGva/2FAFFCHlDcp28qgQXLaW4A6nzn+UiMtwb7r9ZcLchG6dW/xO2m3AVdAW27tYKhtWGBY7ij5C7Pm7dBDOiRkSMuKx0L0+l2adTQ8m59pLgo7yacWFjpbGZFsdUV2Y1L5oM7lcAsPr0O2Xq6Iwncw2dYG9DRo+Mlum6kIe6uCm7DwdrwYtKbBg+d7f+RTwyHvk1TAjWRlA+bnXBEqt22m9B7ASzFo8OJn9+2iIs5EYFIneYVtts4PzUu4m1t1uRtwmgPSzAk1bW1lZ8olEiLVGqE2uORv89gnRtSdV8YnIXV97Ol1eUg0yVReejGt3TqJ2w3AB6rqngbKmH96VdqYaYYzYzOV8vvQUkUWwH5TzcECrym3N1w5AKvgSb+481XO2Fh8BVyamF1zQW6fzS6pEOS9IAle2OP5YA3bGeeaCElW8apDbUYjL5xU8iOMxwX6ojfZ0/rcWNnE5MIun8+wX8yniyB/D2abIVpgH3AOJOUhgR9q+oDYD7EwOrfWca0zTvZRzsx02Sj8pxLG9CchuPDP6Q3SXxq/NvEQVMPpDzzjk4w==",
        })
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Connection": "keep-alive",
            "Cookie": 'aws-target-static-id=1460341173658-788740; aws-target-visitor-id=1460341173661-21096; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=134492BDA8807349-20AB2D7C815E1F64; s_dslv=1460341175322; s_vn=1491877175325%26vn%3D1; s_nr=1460341175326-New; regStatus=pre-register; s_pers=%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271463356822486%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271463356824667%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271463370142563%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271463379458205%2527%255D%255D%7C1621145858205%3B%20s_dl%3D1%7C1463394162574%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1463394162588%3B; session-token="8T847U4eJsMJnDcqjX+RsMBFKFAx9Zp/yPAAqkYVqkjGO43LCH0BA+OLrcnpwn/NM3sSvM8rnAer9u9G3q5IpWYVtv3ISmXd9uWjZ7y7lnC/3t68v5ygEXP6JpVW8UW8421zc1l9JEtkUubZExOqeySAgA1W3lCIg+eIZOfNi775uBHqQQgOtdbirnnPbXO4SJCXXvjHafMO0wo70WgtJUh8jJoji+t3mGeNy7hZnhM="; x-main="FCHU8zL6hZnYzmX?bNCGIOQZ1wXekgJqwJ6g7L1gksWVRoeoBD4mrdA@AfPdbHHA"; at-main=Atza|IQEBLjAsAhRC6nEdui1Q-758tjGAOisMYtdhOQIUJgk_BNnHPm-nGzP7-idSo3s-h_dGdMV5iAtm-5g00_gZwI-pboEdj9WnbDWN1K_6aOevIaH4Qe3_Ex-lYaYfZv1kE0jB6Ri2E0VPy2SMg676PYXE1Kp9Rjj2d-p7E-m20x9oWcMjt4yenzFQBeStl8RRh-QlcgO2Qr8ApBUSKQbxjSUSp4tY_5vugztiMU_MTtXTGmLsuIUKhWPzHvQN9yyCKhZU5mzfGchvMBFQvuHcZOT24nqRsHOz6hCbLEgMbt3aMReXVUEXZ0DRm964RZXXn1uwp7cWXvMoV2GEhdG9YgEZkE6JfGNYx_trDWwjEHdRnRs; sess-at-main="x4W7f6dgWknVW5PLCvaXMtUJI3QTVvtdrl5KtyRTvTk="; csm-hit=564.29|1463396263082; s_sess=%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_cc%3Dtrue%3B%20ev1%3Dn/a%3B%20s_sq%3Damznsrvsprod%252Camznsrvsmainprod%253D%252526pid%25253DUS%2525253ASC%2525253A%25252520SellerCentralLogin%252526pidt%25253D1%252526oid%25253D%252525A0%252525A0%252525u767B%252525u5F55%252525A0%252525A0%2525250A%252526oidt%25253D3%252526ot%25253DSUBMIT%3B; session-id=180-9662177-9190219; session-id-time=1464002338l; ubid-main=187-8952156-1332319',
            "Host": "sellercentral.amazon.com",
            "Referer": "https://sellercentral.amazon.com/gp/homepage.html?ie=UTF8&*Version*=1&*entries*=0&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
        }

    def get_list_html(self, list_link):
        print len(list_link), "----type---list_link---", type(list_link),
        html_list = []
        for i in range(len(list_link)):
            req_url = list_link[i],
            req = urllib2.Request(
                url=req_url,
                data=self.postdata,
                headers=self.headers
            )
            try:
                start_time = datetime.datetime.now()
                print "start--", start_time
                result = urllib2.urlopen(req, timeout=2)
                try:
                    s_r = result.read()
                    gzipped = result.headers.get('Content-Encoding')
                    if gzipped:
                        htmls = zlib.decompress(s_r, 16+zlib.MAX_WBITS)
                        print "time==", datetime.datetime.now() - start_time
                        # print "get_list_html-----", htmls
                        html_list .append(htmls)
                except Exception,e:
                    print "gzipped,......"
            except socket.timeout as e:
                print type(e)
                print "There was an error: %r"
            except urllib2.URLError as e:
                print type(e), "----url ===", req_url
        return html_list

    def get_list(self, html):
        list_link = []
        for i in range(len(html)):
            soup = BeautifulSoup(html[i])
            ul = soup.select("#subtopics a")
            if ul:
                for u in range(len(ul)):
                    link_a = ul[u]
                    # print type(link_a)
                    # print link_a.get("href")
                    # print link_a.string
                    list_link.append(link_a.get("href"))
                # print list_link
                html_list = self.get_list_html(list_link)
                self.get_list(html_list)
        # print "list_link------------", list_link
        return list_link

    def get_info(self, html):
        err_solution = ""
        err_desc = ""
        err_code = 0
        p_error = ""
        pattern = re.compile(r'([0-9]+)')
        for i in range(len(html)):
            soup = BeautifulSoup(html[i])
            try:
                err_code = pattern.findall(soup.h2.string)
                print "page===", i, "------", err_code[0]
                err_desc = soup.find("p", {"class": "code"}).get_text()
                # print "err_desc=======", err_desc
                p_error = soup.find("div", {"id": "_modules"})
            except AttributeError or TypeError as e:
                print "h2, class=code, p_error is not found."
            # if p_error and err_code and err_desc:
            #     for name in p_error:
            #         err_solution = name.get_text().replace(err_desc, "")
            #         # print "err_solution=======", err_solution.replace(" ", "")
            #     with sessionCM() as session:
            #         try:
            #             Amazon_err.create(session, err_code, err_desc, err_solution)
            #         except AttributeError as e:
            #             print "insert filed."
            # else:
            #     print "It isn't final page."

if __name__ == "__main__":
    first = Amazon_errmsg()
    # url=['https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712450_cont_17781?ie=UTF8&itemID=200712450&language=zh_US']
    url = ['https://sellercentral.amazon.com/gp/help/help.html/ref=ag_17781_bred_200712520?ie=UTF8&itemID=17781&language=zh_US']
    # url = ['https://sellercentral.amazon.com/gp/help/help.html/ref=sc_hp_rel_200712050?ie=UTF8&itemID=200712050&language=zh_US']
    # url1003 = ['https://sellercentral.amazon.com/gp/help/help.html/ref=sc_hp_rel_24761?ie=UTF8&itemID=24761&language=zh_US']
    tmp_url = url[0]  #-----
    url.remove(tmp_url)  #-----
    #  防止内存崩溃
    start_t = datetime.datetime.now()
    print "start time,", start_t
    html = first.get_list_html(tmp_url)  #-----
    print "html--", len(html)
    aim_list = first.get_list(html)
    aim_time = datetime.datetime.now()
    print "aim time ,", aim_time - start_t
    print "aim list len----", len(aim_list)
    aim_list_html = first.get_list_html(aim_list)
    print "html time", datetime.datetime.now(), datetime.datetime.now() - aim_time
    first.get_info(aim_list_html)
    print "toal time,", datetime.datetime.now(), datetime.datetime.now() - start_t
