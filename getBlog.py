import urllib3
import re
from datetime import datetime
from bs4 import BeautifulSoup

# kobayashi
url = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=07"

# hirate
#url = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=17"

# for urllib3
http = urllib3.PoolManager()
r = http.request('GET', url)

soup = BeautifulSoup(r.data, "html.parser")

titles_html = soup.select("article > div.innerHead > div.box-ttl > h3 > a")
blogs_html = soup.select("article > div.box-article")

titles = []
blogs = []

for title in titles_html:
    titles.append(title.text)

for blog in blogs_html:
    blogs.append(blog.text)


# for i in range(20):
#     #f = open("./hirate/"+str(i) + '.txt','w')
#     f = open("./kobayashi/"+str(i) + '.txt','w')
#     f.write(blogs[i])
#     f.close()

#print(blogs[3])
