# coding: utf-8
import sys
import pickle
import numpy as np
sys.path.append('../dl-parts')
from common import config
# GPUで実行する場合は下記のコメントアウトを消去（要cupy）
# ==============================================
# config.GPU = True
# ==============================================
from common.optimizer import SGD
from common.trainer import RnnlmTrainer
from common.util import eval_perplexity, to_gpu
from ch06.better_rnnlm import BetterRnnlm


# ハイパーパラメータの設定
batch_size = 20
wordvec_size = 650
hidden_size = 650
time_size = 35
lr = 20.0
max_epoch = 40
max_grad = 0.25
dropout = 0.5

# 学習データの読み込み
name = "sugai"
vocab_path = "../datasets/params_corpus/" + name + ".pkl"
with open(vocab_path, 'rb') as f:
    # params = {"words": words, "corpus": corpus, "word_to_id": word_to_id,\
    # "id_to_word": id_to_word}
    params = pickle.load(f)
corpus_org = params["corpus"]
word_to_id = params["word_to_id"]
id_to_word = params["id_to_word"]

# 8:1:1にcorpusを分割. それぞれtrain, val, test用
div_ratio = len(corpus_org) // 10
corpus = corpus_org[ : div_ratio*8]
corpus_val = corpus_org[div_ratio*8 : div_ratio*9]
corpus_test = corpus_org[div_ratio*9 :]

# list型のcorpusをnumpyの配列ndarrayに変換
corpus = np.array(corpus)
corpus_val = np.array(corpus_val)
corpus_test = np.array(corpus_test)


if config.GPU:
    corpus = to_gpu(corpus)
    corpus_val = to_gpu(corpus_val)
    corpus_test = to_gpu(corpus_test)

vocab_size = len(word_to_id)
xs = corpus[:-1]
ts = corpus[1:]

model = BetterRnnlm(vocab_size, wordvec_size, hidden_size, dropout)
optimizer = SGD(lr)
trainer = RnnlmTrainer(model, optimizer)

best_ppl = float('inf')

sava_path = "../datasets/params_betterRnnlm/" + name + ".pkl"
for epoch in range(max_epoch):
    trainer.fit(xs, ts, max_epoch=1, batch_size=batch_size,
                time_size=time_size, max_grad=max_grad)

    model.reset_state()
    ppl = eval_perplexity(model, corpus_val)
    print('valid perplexity: ', ppl)

    if best_ppl > ppl:
        best_ppl = ppl
        model.save_params(file_name=save_path)
    else:
        lr /= 4.0
        optimizer.lr = lr

    model.reset_state()
    print('-' * 50)


# テストデータでの評価
model.reset_state()
ppl_test = eval_perplexity(model, corpus_test)
print('test perplexity: ', ppl_test)
