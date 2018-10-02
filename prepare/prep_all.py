#### コマンドラインの第一引数にメンバーの名前をローマ字で入れ実行
#### ex. python3 prep_all.py kawata

import sys
import pickle
import os
import getBlogPutCSV
import generateCorpus
sys.path.append('..')
from datasets import member_const

name = sys.argv[1]
names = member_const.names

if name not in names:
    print("[USAGE] python3 prep_all.py NAME_OF_MEMBER")
else:
    path_csv = "../blogs/" + name + "/blogs.csv"
    path_corpus = "../datasets/params_corpus/" + name + ".pkl"

    if not os.path.exists(path_csv):
        print("creating " + name + "'s csv file...")
        getBlogPutCSV.getAndPut(name)
        print("done")

    if not os.path.exists(path_corpus):
        print("creating " + name + "'s corpus file...")
        generateCorpus.gen(name)
        print("done")
