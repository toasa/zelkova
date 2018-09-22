import sys
sys.path.append("..")
import numpy as np
from common import config

# Calc in GPU
# config.GPU = True

import pickle
from common.trainer import Trainer
from common.optimizer import Adam
from cbow import CBOW
from skip_gram import SkipGram
from common.util import create_contexts_target, to_cpu, to_gpu

window_size = 5
hidden_size = 100
batch_size = 100
max_epoch = 10

name = "kobayashi"
vocab_path = "../../datasets/pkl_files/" + name + ".pkl"

with open(vocab_path, 'rb') as f:
    # params = {"words": words, "corpus": corpus, "word_to_id": word_to_id,\
    # "id_to_word": id_to_word}
    params = pickle.load(f)


corpus = params["corpus"]
word_to_id = params["word_to_id"]
id_to_word = params["id_to_word"]

vocab_size = len(word_to_id)

contexts, target = create_contexts_target(corpus, window_size)
if config.GPU:
    contexts, target = to_gpu(contexts), to_gpu(target)

model = CBOW(vocab_size, hidden_size, window_size, corpus)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()

word_vecs = model.word_vecs

if config.GPU:
    word_vecs = to_cpu(word_vecs)

params = {}
params["word_vecs"] = word_vecs.astype(np.float16)
params["word_to_id"] = word_to_id
params["id_to_word"] = id_to_word
pkl_file = "./cbow_params_" + name + ".pkl"

with open(pkl_file, "wb") as f:
    pickle.dump(params, f, -1)
