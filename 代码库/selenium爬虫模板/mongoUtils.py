from pymongo import MongoClient


# .\mongod.exe --dbpath=H:\py7\scrapyxx\guomeiSele\db --port=27011
# 连接mongodb

# 获取一个集合
def get_collection(ip='localhost',
                   port='27011',
                   db_name='hello',
                   collection_name='hello'):
    connection = f'mongodb://{ip}:{port}/'
    client = MongoClient(connection)
    db = client[db_name]
    collection = db[collection_name]
    return collection


# 获取一个数据库
def get_db(ip='localhost',
           port='27011',
           db_name='hello'):
    connection = f'mongodb://{ip}:{port}/'
    client = MongoClient(connection)
    db = client[db_name]
    return db


# 查询数据
def get_data():
    collection = get_collection(db_name='hello',
                                collection_name='hello')
    result = [i for i in collection.find()]

    return result
