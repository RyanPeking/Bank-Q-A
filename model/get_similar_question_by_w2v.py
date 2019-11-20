# 此方法太慢，不满足要求

import time
from model.utils import get_stopwords, get_word2vec, cut, topk, token
import numpy as np
from scipy.spatial.distance import cosine
import pandas as pd


def get_sentence_vec(clean_sentence, stopwords_path, word2vec_path):
    '''
    :param sentence: 分词后的list
    :param stopwords_path:
    :param word2vec_path:
    :return:
    '''
    stopwords = get_stopwords(stopwords_path)
    # clean_sentence = remove_stopwords(sentence, stopwords)
    if len(clean_sentence) == 0:
        raise Exception('请重新输入您的需求...')
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


def get_sentences_cos(sentence_vec1, sentence_vec2):
    return cosine(sentence_vec1, sentence_vec2)


def get_similiar_qa(query, qa_path, k, stopwords_path, word2vec_path):
    query = token(query)
    query = cut(query)
    query_vec = get_sentence_vec(query, stopwords_path, word2vec_path)
    qa = pd.read_csv(qa_path)
    distances = []
    for q, a in zip(qa['q_cutwords'], qa['answer']):
        question_vec = get_sentence_vec(q.split(), stopwords_path, word2vec_path)
        cos = get_sentences_cos(query_vec, question_vec)
        distances.append((cos, q, a))
    return topk(distances, k)


if __name__ == '__main__':
    strat = time.time()
    query = '转账'
    k = 4
    import os
    root_path = os.path.abspath('./')
    qa_path = os.path.join(root_path, 'dataset', 'clean_qa_corpus.csv')
    stopwords_path = os.path.join(root_path, 'dataset', 'stop_words.txt')
    word2vec_path = os.path.join(root_path, 'dataset', 'word2vec.model')
    print(get_similiar_qa(query, qa_path, k, stopwords_path, word2vec_path))
    end = time.time()
    print(end-strat)




