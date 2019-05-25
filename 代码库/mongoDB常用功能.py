from pymongo import MongoClient
import re
import pandas as pd
# 进入mongodb安装位置
# .\mongod.exe --dbpath=H:\py7\weiboFlaskVis\db --port=27017
# 连接mongodb

# 获取一个集合
def get_collection(ip='localhost',
                   port='27017',
                   db_name='Sina',
                   collection_name='weibo'):
    connection = f'mongodb://{ip}:{port}/'
    client = MongoClient(connection)
    db = client[db_name]
    collection = db[collection_name]
    return collection


# 查询指定数据
def get_data(keyword):
    collection = get_collection()
    myquery = {"title": re.compile(keyword)}
    result = list(collection.find(myquery).limit(50))
    df = pd.DataFrame(result)
    df = df.drop(columns=['_id'])
    return df

# 查询所有数据
def get_data(keyword):
    collection = get_collection()
    myquery = {"title": re.compile(keyword)}
    result = list(collection.find(myquery).limit(50))
    df = pd.DataFrame(result)
    df = df.drop(columns=['_id'])
    return df