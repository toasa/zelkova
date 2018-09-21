# coding: UTF-8
import pickle

name = "kobayashi"
vocab_path = "./datasets/pkl_files/" + name + ".pkl"

with open(vocab_path, 'rb') as f:
    # params = {"words": words, "corpus": corpus, "word_to_id": word_to_id,\
    # "id_to_word": id_to_word}
    params = pickle.load(f)

words = params["word_to_id"]
corpus = params["corpus"]
word_to_id = params["word_to_id"]
id_to_word = params["id_to_word"]

print(word_to_id)
