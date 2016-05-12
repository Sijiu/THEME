# -*- coding: utf-8 -*-

import urllib
import urllib2
import gzip, StringIO, zlib
from reg import MyHTMLParser
import re
postdata = urllib.urlencode({
    "widgetToken": "X2VuY29kaW5nPVVURjgmbGFuZ3VhZ2U9emhfQ04mb3BlbmlkLmFzc29jX2hhbmRsZT1zY19uYV9hbWF6b24mb3BlbmlkLmNsYWltZWRfaWQ9aHR0cCUzQSUyRiUyRnNwZWNzLm9wZW5pZC5uZXQlMkZhdXRoJTJGMi4wJTJGaWRlbnRpZmllcl9zZWxlY3Qmb3BlbmlkLmlkZW50aXR5PWh0dHAlM0ElMkYlMkZzcGVjcy5vcGVuaWQubmV0JTJGYXV0aCUyRjIuMCUyRmlkZW50aWZpZXJfc2VsZWN0Jm9wZW5pZC5tb2RlPWNoZWNraWRfc2V0dXAmb3BlbmlkLm5zPWh0dHAlM0ElMkYlMkZzcGVjcy5vcGVuaWQubmV0JTJGYXV0aCUyRjIuMCZvcGVuaWQubnMucGFwZT1odHRwJTNBJTJGJTJGc3BlY3Mub3BlbmlkLm5ldCUyRmV4dGVuc2lvbnMlMkZwYXBlJTJGMS4wJm9wZW5pZC5wYXBlLm1heF9hdXRoX2FnZT0wJm9wZW5pZC5yZXR1cm5fdG89aHR0cHMlM0ElMkYlMkZzZWxsZXJjZW50cmFsLmFtYXpvbi5jb20lMkZncCUyRmhlbHAlMkZoZWxwLmh0bWwlM0ZpZSUzRFVURjglMjZpdGVtSUQlM0QxNzc4MSUyNmxhbmd1YWdlJTNEemhfVVMlMjZyZWZfJTNEYWdfMTc3ODFfYnJlZF8zMDYwMSZwYWdlSWQ9c2NfbmFfYW1hem9uJnNob3dSbXJNZT0w:cGxwbE14MEVhUnlDVENweTNueEpPZXhkbUtmMEwwT2tKRnRjcUlWK3kyWT06MQ==",
    "rememberMe": "false",
    "username": "yangguoli@actneed.com",
    "password": "yaya2015",
    "sign-in-button": "",
    "metadata1": "OIwpGZoo1E6M203NKSfmoeknjsR5d33e1TzgHq9YfV8oCZ/XgZ0GADuoIvfUjtGapQ03NvqgxlUIDuwxZ8tqpxWtcB7eJDtxUzH46QppFCI4m3htBg80dZhVTkI7z3T5ksk+lLVOkaFstk3iIgzj0uwFoEU9x0Q9JOHvKu4u1c2pdDMtOEJOwQb0e6x/H9/jogqp5jP574i2RTpfLy9V6WnU9x1rexfE4k1g35Gpkmcr1alxTDKq2SgyyYGTgaghxusEGva/2FAFFCHlDcp28qgQXLaW4A6nzn+UiMtwb7r9ZcLchG6dW/xO2m3AVdAW27tYKhtWGBY7ij5C7Pm7dBDOiRkSMuKx0L0+l2adTQ8m59pLgo7yacWFjpbGZFsdUV2Y1L5oM7lcAsPr0O2Xq6Iwncw2dYG9DRo+Mlum6kIe6uCm7DwdrwYtKbBg+d7f+RTwyHvk1TAjWRlA+bnXBEqt22m9B7ASzFo8OJn9+2iIs5EYFIneYVtts4PzUu4m1t1uRtwmgPSzAk1bW1lZ8olEiLVGqE2uORv89gnRtSdV8YnIXV97Ol1eUg0yVReejGt3TqJ2w3AB6rqngbKmH96VdqYaYYzYzOV8vvQUkUWwH5TzcECrym3N1w5AKvgSb+481XO2Fh8BVyamF1zQW6fzS6pEOS9IAle2OP5YA3bGeeaCElW8apDbUYjL5xU8iOMxwX6ojfZ0/rcWNnE5MIun8+wX8yniyB/D2abIVpgH3AOJOUhgR9q+oDYD7EwOrfWca0zTvZRzsx02Sj8pxLG9CchuPDP6Q3SXxq/NvEQVMPpDzzjk4w==",
})
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Connection": "keep-alive",
    "Cookie": 'aws-target-static-id=1460341173658-788740; aws-target-visitor-id=1460341173661-21096; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=134492BDA8807349-20AB2D7C815E1F64; s_dslv=1460341175322; s_vn=1491877175325%26vn%3D1; s_nr=1460341175326-New; regStatus=pre-register; s_pers=%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271463041554137%2527%255D%255D%7C1620807954137%3B%20s_dl%3D1%7C1463052760967%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1463052760969%3B; session-token="py7BalNadrdsddpvskAd9KldjUyeQLgX37tn5ielnwYxOTWwM5Tyv35SY74LEtxYRSBWkF0rCDY3Q6YeyxqfVNledcEiGLYt3oNUMtKXf+SdNU/jlGQnbPqXxV6rwhC5ghv4dzS5xvx8PuPKdQH+7P8wilbKSHIZjLTlSt6wMApY+SsCX5Kit1YqVrk0FfeVLra+nWUgONB/BKfRID45Irs+D/S4+dMiWKPbNCtAEOp/mn3ztCX2Anzg59SiOku7PvhUawwTHWbjeD2QRhlTgg=="; x-main="DiOzYbJCcQyzrDkAQU?8ASOalSkTZVAM2TbKb9145cMRZDQJWJlxPKcSycdducN?"; at-main=Atza|IQEBLjAsAhQml246fV6wy_FN6uYbjKWnz-bEzAIUVyI0n56yuRGKdxbkLClzVeHh_eFVdH3b73M282HnYKvJuGBcSYVaQGWXCZnZxHEH8Cs0Cr5STV5uQjP91LB7UmD4IKnsMhuYee05cjKoIGB2bKmUWDYlqT_vSmHIY4bWsNVJZ5XBKbrgkMmMvkJkuk59_xzMhdXXLoaiZ9ldrHe6uh4Iysf6Sd2KIyS65ByGiYQkn0N54FirVedf-0l4hClxRtztBQllTn53gDRdH6c2nKZF0kRzEdX7wRMJ1VaUmXdt45jeeInb_bgEWmBJEsJhu61pVf6xSdJcUZV_xtw5ldBWIR2pw3X_zIHeUT4QTBnVeL8; sess-at-main="fU7DKKfaP6f+vpABW82qwxS7lgpGK0EiwyYY75Crn5U="; csm-hit=133.80|1463051011077; session-id=184-2015367-1084624; session-id-time=1463656169l; s_sess=%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_cc%3Dtrue%3B%20ev1%3Dn/a%3B%20s_sq%3Damznsrvsprod%252Camznsrvsmainprod%253D%252526pid%25253DUS%2525253ASC%2525253A%25252520SellerCentralLogin%252526pidt%25253D1%252526oid%25253D%252525A0%252525A0%252525u767B%252525u5F55%252525A0%252525A0%2525250A%252526oidt%25253D3%252526ot%25253DSUBMIT%3B; ubid-main=188-3123239-9402116',
    "Host": "sellercentral.amazon.com",
    "Referer": "https://sellercentral.amazon.com/gp/homepage.html?ie=UTF8&*Version*=1&*entries*=0&",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
}
req = urllib2.Request(
    url='https://sellercentral.amazon.com/gp/help/help.html/ref=ag_17781_bred_30601?ie=UTF8&itemID=17781&language=zh_US',
    # url='https://sellercentral.amazon.com/gp/help/help.html/ref=ag_22951_cont_17781?ie=UTF8&itemID=22951&language=zh_US',
    data=postdata,
    headers=headers
)
result = urllib2.urlopen(req)
# result.add_header('Accept-encoding', 'gzip')
# opener = urllib2.build_opener()
# response = opener.open(result)html = response.read()

gzipped = result.headers.get('Content-Encoding')
if gzipped:
    html = zlib.decompress(result.read(), 16+zlib.MAX_WBITS)
hp = MyHTMLParser()
hp.feed(html)
hp.close()
print html
print hp.links
# print "--", result.read()
# SERIA = re.compile(r'<div id="subtopics"><ul>.*</ul>\s?</div>')
# result1 = re.match(SERIA, html)
# print "result==", result1
