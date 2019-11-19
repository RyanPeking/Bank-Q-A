from utils import get_stopwords, get_word2vec, cut, remove_stopwords, findKsmallest
import numpy as np
from scipy.spatial.distance import cosine
import pandas as pd


def get_sentence_vec(text, stopwords_path, word2vec_path):
    sentence = cut(text)
    stopwords = get_stopwords(stopwords_path)
    clean_sentence = remove_stopwords(sentence, stopwords)
    word2vec = get_word2vec(word2vec_path)
    oovs = {}
    sentence_vec = np.zeros_like(word2vec.wv['测试'])

    for word in clean_sentence:
        if word in word2vec.wv.vocab:
            sentence_vec += word2vec.wv[word]
        elif word in oovs:
            sentence_vec += oovs[word]
        else:
            oovs[word] = np.random.random(word2vec.wv['测试'].shape)

    sentence_vec = sentence_vec / len(clean_sentence)

    return sentence_vec


def get_sentences_cos(sentence1, sentence2, stopwords_path, word2vec_path):
    sentence_vec1 = get_sentence_vec(sentence1, stopwords_path, word2vec_path)
    sentence_vec2 = get_sentence_vec(sentence2, stopwords_path, word2vec_path)
    return cosine(sentence_vec1, sentence_vec2)


def get_similiar_qa(query, qa_path, k, stopwords_path, word2vec_path):
    qa = pd.read_csv(qa_path)
    distances = []
    for q, a in zip(qa['question'], qa['answer']):
        cos = get_sentences_cos(query, q, stopwords_path, word2vec_path)
        distance = (cos, q, a)
        distances.append(distance)
    return findKsmallest(distances, k)


if __name__ == '__main__':
    query = '转账'
    k = 4
    import os
    root_path = os.path.abspath('./')
    qa_path = os.path.join(root_path, 'dataset', 'clean_qa_corpus.csv')
    stopwords_path = os.path.join(root_path, 'dataset', 'stop_words.txt')
    word2vec_path = os.path.join(root_path, 'dataset', 'word2vec.model')
    print(get_similiar_qa(query, qa_path, k, stopwords_path, word2vec_path))




