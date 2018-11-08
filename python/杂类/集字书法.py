# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:45:16 2018

@author: Administrator
"""

'''
1. 读取文章
2. 将文章编号
3. 将文章set化
4. 获取文字数据，无数据的放入err_list
5. 将文字分组
6. 挑出特定作者的文字，并计入done_list
7. 从无特定作者的样本中排除done_list中的文字，然后再随机选择
8. 将两组数据合并
9. 按原始文章顺序排列文字
'''
import pandas as pd
from os.path import join as joinpath
def read_text(fpath):
    '''
    return:
        list_text
        list_order
    '''
    with open(fpath, 'r') as f:
        data = ''.join(f.readlines)
        list_text = []
        list_order = []
    for i in range(len(data)):
        list_text.append(data[i])
        list_order.append(i)
    return list_text

def get_mongo_collection():
    pass
#    return collection

def get_char_pics(char):
    pass
    # return pd.DataFrame([i for i in result])

def get_data(txt):
    fnl = pd.DataFrame()
    err_list = []
    for char in txt:
        tmp = get_char_pics(char)
        if len(tmp)>0:
            fnl = pd.concat([fnl, tmp])
        else:
            err_list.append(char)
    return fnl, err_list

def choose_char(df_raw):
    df = df_raw.copy()
    df['rn'] = df.groupby(['author']).cumcount()
    df = df[df['rn'] == 1]
    return df
def get_result(fpath,author_list ):
    list_text = read_text(fpath)
    txt = set(list_text)
    fnl, err_list = get_data(txt)

    fnl['tmp'] = fnl['author'].apply(lambda x:1 if x in author_list else 0)
    fnl_good = fnl[fnl.tmp == 1]
    fnl_bad = fnl[fnl.tmp == 0]


    fnl_good = choose_char(fnl_good)
    find_words = set(fnl_good['author'])
    fnl_bad['tmp'] = fnl_bad['author'].apply(lambda x:1 if x in find_words else 0)
    fnl_bad = choose_char(fnl_bad)
    fnl = pd.concat([fnl_good, fnl_bad])

    fnl_list = []
    for i in list_text:
        tmp = fnl['char'][fnl['char'] == i].iloc[0]
        fnl_list.append(tmp)
    return fnl_list, err_list, list_text
if __name__ == '__main__':
    fpath = r''
    author_list = []
    save_dir = r''
    fnl_list, err_list, list_text = get_result(fpath,author_list)
    ii = 0
    for char in fnl_list:
        if char not in err_list:
            with open(joinpath(save_dir, str(ii) + list_text[ii]+'.gif'), 'wb') as f:
                f.write(char)
        ii+=1

    print(err_list)
    
