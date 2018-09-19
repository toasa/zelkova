import urllib3
import re
from datetime import datetime
from bs4 import BeautifulSoup

# kobayashi ct=07
url_org = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&cd=member&ct=07&page="

for i in range(1):
    url = url_org + str(i)

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, "html.parser")

    titles_html = soup.select("article > div.innerHead > div.box-ttl > h3 > a")
    blogs_html = soup.select("article > div.box-article")

    # nth-childではうまく動かない
    # dates_html = soup.select("article > div.box-bottom > ul > li:nth-child(1)")
    dates_html = soup.select("article > div.box-bottom > ul > li:nth-of-type(1)")

    titles = []
    blogs = []
    dates = []

    for title in titles_html:
        titles.append(title.text)

    for blog in blogs_html:
        blogs.append(blog.text)

    for date in dates_html:
        dates.append(date.text.strip)

    print(dates[0])




# # for urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', url)
#
# soup = BeautifulSoup(r.data, "html.parser")
#
# titles_html = soup.select("article > div.innerHead > div.box-ttl > h3 > a")
# blogs_html = soup.select("article > div.box-article")
#
# titles = []
# blogs = []
#
# for title in titles_html:
#     titles.append(title.text)
#
# for blog in blogs_html:
#     blogs.append(blog.text)
#
# for i in range(20):
#     #f = open("./hirate/"+str(i) + '.txt','w')
#     f = open("./kobayashi/"+str(i) + '.txt','w')
#     f.write(blogs[i])
#     f.close()
