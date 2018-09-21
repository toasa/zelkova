import pickle

name = "suzumoto"
vocab_path = "../datasets/pkl_files/" + name + ".pkl"

with open(vocab_path, 'rb') as f:
    # params = {"words": words, "corpus": corpus, "word_to_id": word_to_id,\
    # "id_to_word": id_to_word}
    params = pickle.load(f)

print(params["word_to_id"])
