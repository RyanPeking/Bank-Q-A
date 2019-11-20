import pandas as pd
from model.utils import topk


def Edit_Distance(str1, str2):
    """
    计算字符串 str1 和 str2 的编辑距离
    :param str1
    :param str2
    :return:
    """
    # i+j的原因主要是为了记录0行0列的数据，其他的都会在后面替换成正确的值
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if (str1[i - 1] == str2[j - 1]):
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)

    return matrix[len(str1)][len(str2)]


def get_similiar_qa(query, qa_path, k):
    qa = pd.read_csv(qa_path)
    distances = []
    for q, a in zip(qa['q_cutwords'], qa['answer']):
        q = q.split()
        if query in q:
            q = ''.join(q)
            edit_distance = Edit_Distance(query, q)
            distances.append((edit_distance, q, a))
    if distances == []:
        return None
    return topk(distances, k)


if __name__ == '__main__':
    query = '转账'
    k = 10
    import os
    root_path = os.path.abspath('./')
    qa_path = os.path.join(root_path, 'dataset', 'clean_qa_corpus.csv')
    print(get_similiar_qa(query, qa_path, k))