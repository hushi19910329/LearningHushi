# 文本

def load_text(path,encoding='gbk'):
    ''' 说明
    直接读取，不去掉换行符
    '''
    with open(path, 'r', encoding=encoding) as f:
        data = f.readlines()
    return data
    
    
def load_text2(path,encoding='gbk'):
    ''' 说明
    直接读取，去掉换行符
    '''
    with open(path, 'r', encoding=encoding) as f:
        data = [i.strip('\n') for i in f.readlines()]
    return data


def load_stopwords():
    '''说明
    加载停用词
    '''
    path = 'stopwords.txt'
    data = load_text2(path)
    stopwords_list = list(set(data))
    return stopwords_list


import re
import jieba

def clean_data(text):
    '''说明
    中文句子清理
    '''
    text = re.sub('[^\u4e00-\u9fff]+', '', text)
    text = re.sub(r'\d+', ' ', text)  # 去掉数字
    text = re.sub(r'\s+', ' ', text)  # 去掉多个空格

    word_list = list(jieba.cut(text))
    word_list = ' '.join(word_list)
    return word_list