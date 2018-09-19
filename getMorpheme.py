# coding: UTF-8
import re
import MeCab
import codecs


tagger = MeCab.Tagger("-Owakati")
# tagger = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

#f = open("./hirate/0.txt")
f = open("./kobayashi/10.txt")

data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
lines1 = data1.split()
for line in lines1:
    temp = tagger.parse(line).split()
    print(temp)
