import sys
sys.path.append("../dl-parts")
from common.util import most_similar
import pickle

name = "shida"

pkl_file = "../datasets/params_cbow/" + name + ".pkl"

with open(pkl_file, "rb") as f:
    params = pickle.load(f)
    word_vecs = params["word_vecs"]
    word_to_id = params["word_to_id"]
    id_to_word = params["id_to_word"]


querys = ["私", "今日", "鈴本"]
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)
