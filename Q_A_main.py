from model.get_similar_question_by_boolean import get_similiar_qa
import os

query = '转账'
k = 10

root_path = os.path.abspath('./')
qa_path = os.path.join(root_path, 'dataset', 'clean_qa_corpus.csv')
vocab_path = os.path.join(root_path, 'dataset', 'words_frequences.txt')
q_codes_path = os.path.join(root_path, 'dataset', 'q_codes.pk')

res = get_similiar_qa(query, vocab_path, qa_path, q_codes_path, k)
print(res)
