# ブログの日付、タイトル、文章を取得し、著者名のディレクトリ内にcsvファイルとして格納する

import urllib3
import re
import csv
import sys
sys.path.append('..')
from datasets import member_const
import os
from datetime import datetime
from bs4 import BeautifulSoup

# 取得するブログポストの著者を指定
# name = "shida"

def getAndPut(name):
    # 指定したメンバーのブログurlを生成
    url_org = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&cd=member&ct="
    name_id = member_const.name_to_id[name]
    # {0:02d}は桁揃え
    #  5 => 05, 15 => 15
    url_org += "{0:02d}".format(name_id) + "&page="

    # csvファイルを格納するディレクトリの作成
    # 作成済の場合、FileExistsError例外が発生
    try:
        dir_path = "../blogs/" + name
        os.mkdir(dir_path)
    except:
        pass

    http = urllib3.PoolManager()

    titles = []
    blogs = []
    dates = []

    i = 0
    while True:

        url = url_org + str(i)

        r = http.request('GET', url)
        soup = BeautifulSoup(r.data, "html.parser")

        title_tags_html = soup.select("title")
        c = title_tags_html[0].text[0]

        # urlにブログポストがない場合, titleタグの中身は
        # "欅坂46 公式ブログ | 欅坂46公式サイト"
        # となる. cはその一文字目を代入し、比較を行っている
        if c != "欅":
            print("i: ", i, c)
            titles_html = soup.select("article > div.innerHead > div.box-ttl > h3 > a")
            blogs_html = soup.select("article > div.box-article")

            # nth-childではうまく動かない
            # dates_html = soup.select("article > div.box-bottom > ul > li:nth-child(1)")
            dates_html = soup.select("article > div.box-bottom > ul > li:nth-of-type(1)")

            for title in titles_html:
                titles.append(title.text)

            for blog in blogs_html:
                blogs.append(blog.text)

            for date in dates_html:
                dates.append(date.text.strip())

            i += 1

        else:
            print("i: ", i, c)
            break


    # with構文を使うと、close()の呼び出しが不要
    with open('../blogs/' + name + '/blogs.csv', 'w') as csv_f:
        fieldnames = ['date', 'title', 'blog']
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(titles)):
            writer.writerow({'date': dates[i], 'title': titles[i], 'blog': blogs[i]})
