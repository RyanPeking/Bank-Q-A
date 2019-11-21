from model.utils import cut, token, topk
import pandas as pd
from model.get_similar_question_by_edit_distance import Edit_Distance


def get_code(query, vocab):
    query = cut(query)
    # vocab = load_pickle(vocab_path)
    code = 0
    for word in query:
        try:
            _id = vocab.word_to_id(word)
        # oov
        except:
            continue
        code |= 1 << _id
    return code


def get_similiar_qa(query, vocab, qa_path, q_codes, k):
    qa = pd.read_csv(qa_path)
    query = token(query)
    query_code = get_code(query, vocab)

    res = []
    for i, (q, a) in enumerate(zip(qa['question'], qa['answer'])):
        code_and = query_code & q_codes[i]
        if code_and == 0:
            continue

        # 得到code_and中1位的个数
        # same_words_num = 0
        # while code_and:
        #     if code_and & 1:
        #         same_words_num += 1
        #     code_and >>= 1
        # res.append((same_words_num, q, a))
        res.append((q, a))

    if res == []:
        return None

    distances = []
    # 根据布尔搜索的结果，按编辑距离排序给出最后答案
    for q, a in res:
        edit_distance = Edit_Distance(query, q)
        distances.append((edit_distance, q, a))
    return sorted(topk(distances, k), key=lambda x: x[0])


# if __name__ == '__main__':
#     strat = time.time()
#     query = '银行卡开户'
#     k = 10
#     import os
#     root_path = os.path.abspath('../')
#     qa_path = os.path.join(root_path, 'dataset', 'clean_qa_corpus.csv')
#     # vocab_path = os.path.join(root_path, 'dataset', 'vocab.pk')
#     vocab_path = os.path.join(root_path, 'dataset', 'words_frequences.txt')
#     q_codes_path = os.path.join(root_path, 'dataset', 'q_codes.pk')
#     res = get_similiar_qa(query, vocab_path, qa_path, q_codes_path, k)
#     print(len(res), res)
#     end = time.time()
#     print(end-strat)
