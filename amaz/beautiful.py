# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from bs4 import BeautifulSoup
import re
from furion.lib.model.amazon_err import Amazon_err
from furion.lib.model.session import sessionCM

html = """
        <div style="margin: 1em; " id="_modules"><div id="subtopics"><ul>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_30601_cont_17781?ie=UTF8&amp;itemID=30601&amp;language=zh_US">错误 15</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_22951_cont_17781?ie=UTF8&amp;itemID=22951&amp;language=zh_US">错误 3015</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200557810_cont_17781?ie=UTF8&amp;itemID=200557810&amp;language=zh_US">错误 4000</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712450_cont_17781?ie=UTF8&amp;itemID=200712450&amp;language=zh_US">5000 系列错误代码</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_201440690_cont_17781?ie=UTF8&amp;itemID=201440690&amp;language=zh_US">8000 系列错误代码</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_31601_cont_17781?ie=UTF8&amp;itemID=31601&amp;language=zh_US">错误 10018</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_24761_cont_17781?ie=UTF8&amp;itemID=24761&amp;language=zh_US">错误 11003</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712510_cont_17781?ie=UTF8&amp;itemID=200712510&amp;language=zh_US">13000 系列错误代码</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712520_cont_17781?ie=UTF8&amp;itemID=200712520&amp;language=zh_US">18000 系列错误代码</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712530_cont_17781?ie=UTF8&amp;itemID=200712530&amp;language=zh_US">20000 系列错误代码</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712500_cont_17781?ie=UTF8&amp;itemID=200712500&amp;language=zh_US">30000 系列错误代码</a>
        <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712050_cont_17781?ie=UTF8&amp;itemID=200712050&amp;language=zh_US">90000 系列错误代码</a>
        </ul>
    """
a_html = """
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_30601_cont_17781?ie=UTF8&amp;itemID=30601&amp;language=zh_US">错误 15</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_22951_cont_17781?ie=UTF8&amp;itemID=22951&amp;language=zh_US">错误 3015</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200557810_cont_17781?ie=UTF8&amp;itemID=200557810&amp;language=zh_US">错误 4000</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712450_cont_17781?ie=UTF8&amp;itemID=200712450&amp;language=zh_US">5000 系列错误代码</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_201440690_cont_17781?ie=UTF8&amp;itemID=201440690&amp;language=zh_US">8000 系列错误代码</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_31601_cont_17781?ie=UTF8&amp;itemID=31601&amp;language=zh_US">错误 10018</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_24761_cont_17781?ie=UTF8&amp;itemID=24761&amp;language=zh_US">错误 11003</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712510_cont_17781?ie=UTF8&amp;itemID=200712510&amp;language=zh_US">13000 系列错误代码</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712520_cont_17781?ie=UTF8&amp;itemID=200712520&amp;language=zh_US">18000 系列错误代码</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712530_cont_17781?ie=UTF8&amp;itemID=200712530&amp;language=zh_US">20000 系列错误代码</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712500_cont_17781?ie=UTF8&amp;itemID=200712500&amp;language=zh_US">30000 系列错误代码</a>
    <a href="https://sellercentral.amazon.com/gp/help/help.html/ref=ag_200712050_cont_17781?ie=UTF8&amp;itemID=200712050&amp;language=zh_US">90000 系列错误代码</a>
"""

page = """
       <h2 class="page"> 错误 99104</h2>
<div style="margin: 1em; " id="_modules"><p class="header-orange"><a name="200713660"></a></p><html-content><p class="code">{0} 的值与已经和所给 SKU {1} 关联的 ASIN 不匹配。请在发送此记录前提供正确的 ASIN-提示或删除现有的 SKU。</p>
<p>（错误）您的输入文件中一个值与已经和所给 ASIN 关联的 ASIN 不匹配。选择其一：</p>
<ul>
  <li>为已经与所给 SKU 关联的 ASIN 提供一个 ASIN 提示，并重新提交输入数据。</li>
  <li>删除现有的 SKU 并重新提交输入数据。</li>
</ul>如果您想更改所给 SKU 的 ASIN，可删除 SKU 并等待 24 小时后再提交具有新 ASIN 的 SKU。
<br/>
</html-content></div>
     </td>
"""


soup = BeautifulSoup(page)
errcode_str = soup.h2.string
pattern = re.compile(r'([0-9]+)')
err_code = pattern.findall(errcode_str)
print err_code[0]
err_solution = ""
err_desc = ""
# p_err = soup.select("p")
# for i in range(len(p_err)):
#     # print i, "---", p_err[i].string
#     print  i, "---", p_err[i].get_text()
#     if i == 1:
#         # err_desc = p_err[i].string
#         err_desc = p_err[i].get_text()
#     elif i > 1:
#         if p_err[i].string:
#             # err_solution += p_err[i].string
#             err_solution += p_err[i].get_text()
# err_code = err_code[0]
# with sessionCM() as session:
#     Amazon_err.create(session, err_code, err_desc, err_solution)

# err_desc = soup.find("p", {"class": "code"}).get_text()
# print "siblings---", err_desc
# p_error = soup.find("div", {"id": "_modules"})
# for name in p_error:
#     err_solution = name.get_text().replace(err_desc, "")
#     print "error--", err_solution.replace(" ", "")

# err_code = err_code[0]
# with sessionCM() as session:
#     Amazon_err.create(session, err_code, err_desc, err_solution)

