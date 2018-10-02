# coding: utf-8
import sys
import pickle
import random
sys.path.append('../dl-parts')
from common.np import *
from ch07.rnnlm_gen import BetterRnnlmGen

# name: メンバーを指定
# start_word: 生成するブログの一単語目を指定
# (ランダムな単語から文字を始めたいときはstart_word=""とする)
# sample_size: 生成するブログの文字数

name = "hirate"
start_word = ""
sample_size = 200


# 学習データの読み込み
vocab_path = "../datasets/params_corpus/" + name + ".pkl"
with open(vocab_path, 'rb') as f:
    # params = {"words": words, "corpus": corpus, "word_to_id": word_to_id,\
    # "id_to_word": id_to_word}
    params = pickle.load(f)
corpus = params["corpus"]
word_to_id = params["word_to_id"]
id_to_word = params["id_to_word"]

vocab_size = len(word_to_id)
corpus_size = len(corpus)

model = BetterRnnlmGen(vocab_size=vocab_size)
load_path = '../datasets/params_betterRnnlm/' + name + '.pkl'
model.load_params(file_name=load_path)


# start文字とskip文字の設定
if start_word == "":
    start_id = random.choice(corpus)
else:
    start_id = word_to_id[start_word]
# skip_words = ['N', '<unk>', '$']
skip_words = []
skip_ids = [word_to_id[w] for w in skip_words]


# 文章生成
word_ids = model.generate(start_id, skip_ids, sample_size = sample_size)
txt = ''.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')

print(txt)
