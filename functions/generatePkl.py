### Generate pickle file that is dict {words:, corpus: , word_to_id: , id_to_word: }.
### Func of "generatePkl()" generates the above pickle file in the place
### WHERE is called this function.

import csv
import MeCab
import pickle

#name = "kobayashi"

def gen(name):
    #csvファイルの読み込み
    path = "../blogs/" + name + "/blogs.csv"
    csv_file = open(path, "r", encoding="utf_8", errors="", newline="")

    f = csv.reader(csv_file, delimiter=",", doublequote=True,\
     lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    tagger = MeCab.Tagger("-Owakati")

    texts = []
    # cnt = 0
    for row in f:
    #     if cnt == 350:
    #         break
        # 各rowは['date', 'title', 'blog']を格納したリスト
        tmp = tagger.parse(row[2]).split()
        texts.append(tmp)
        # cnt += 1

    texts = texts[1:]

    words = []
    for i in range(len(texts)):
        words += texts[i]

    word_to_id = {}
    id_to_word = {}
    for i, word in enumerate(words):
        if word not in word_to_id:
            tmp_id = len(word_to_id)
            word_to_id[word] = tmp_id
            id_to_word[tmp_id] = word

    corpus = [word_to_id[w] for w in words]

    params = {}
    params["words"] = words
    params["corpus"] = corpus
    params["word_to_id"] = word_to_id
    params["id_to_word"] = id_to_word

    file_path = "../datasets/pkl_files/" + name + ".pkl"
    with open(file_path, "wb") as f:
        pickle.dump(params, f, -1)
