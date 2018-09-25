# coding: utf-8
import sys
import pickle
sys.path.append('..')
from common.np import *
from rnnlm_gen import BetterRnnlmGen


# 学習データの読み込み
name = "kobayashi"
vocab_path = "../../datasets/params_corpus/" + name + ".pkl"
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
model.load_params(file_name='../ch06/zelkova_trained_weight_better_rnnlm_kobayashi.pkl')

# start文字とskip文字の設定
start_word = '洋服'
start_id = word_to_id[start_word]
# skip_words = ['N', '<unk>', '$']
skip_words = []
skip_ids = [word_to_id[w] for w in skip_words]
# 文章生成

word_ids = model.generate(start_id, skip_ids)
txt = ''.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')

print(txt)


# model.reset_state()
#
# start_words = 'the meaning of life is'
# start_ids = [word_to_id[w] for w in start_words.split(' ')]
#
# for x in start_ids[:-1]:
#     x = np.array(x).reshape(1, 1)
#     model.predict(x)
#
# word_ids = model.generate(start_ids[-1], skip_ids)
# word_ids = start_ids[:-1] + word_ids
# txt = ' '.join([id_to_word[i] for i in word_ids])
# txt = txt.replace(' <eos>', '.\n')
# print('-' * 50)
# print(txt)
