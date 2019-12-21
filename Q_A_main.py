from model.get_similar_question_by_boolean import get_similiar_qa
import os
import pickle
from model.data import Vocab


k = 10
root_path = os.path.abspath('./')
qa_path = os.path.join(root_path, 'dataset', 'clean_qa_corpus.csv')
words_frequences_path = os.path.join(root_path, 'dataset', 'words_frequences.txt')
# vocab_path = os.path.join(root_path, 'dataset', 'vocab.pk')
q_codes_path = os.path.join(root_path, 'dataset', 'q_codes.pk')


def load_pickle(path):
    f = open(path, 'rb')
    data = pickle.load(f)
    return data

# 加载q_codes和vocab
q_codes = load_pickle(q_codes_path)
# vocab = load_pickle(vocab_path)
vocab = Vocab(words_frequences_path)

def queryAnswer(query):
    return get_similiar_qa(query, vocab, qa_path, q_codes, k)

# print("您好，我是智能客服小龙人，请问有什么能帮助您的。您可输入您需要办理的业务，例如：银行卡开户。")
# while True:
#     query = input()
#     res = get_similiar_qa(query, vocab, qa_path, q_codes, k)

#     if res == None:
#         print("对不起，小龙人暂时没有该功能呢")

#     # 编辑距离为0，返回答案，否则返回相似问题，让用户确认答案
#     if res[0][0] == 0:
#         print(res[0][2])
#     else:
#         print('请选择您需要办理的业务：')
#         for qa in res:
#             print(qa[1])

