from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import _pickle as pickle
# 划分训练集和测试集
xtrain,xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)


clf = RandomForestClassifier()
clf.fit(xtrain, ytrain)
yhat = clf.predict(xtest)
print(classification_report(ytest, yhat))

# 模型持久化
with open('model/rf_model','wb') as f:
    f.write(pickle.dumps(clf))
    
# 加载 本地 模型
with open('model/rf_model','wb') as f:
    clf = pickle.load(f)
    
# 类别与int映射
label_to_int = {label:i for i, label in enumerate(data_list)}
int_to_label = {v: k for k, v in label_to_int.items()}


# tfidf特征
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    max_df=1.0,
    min_df=2,
    max_features=60,
    binary=True,
    stop_words=stopwords)
tfidf.fit(x_text)
x = tfidf.transform(x_text).toarray()


data_d = {
    'x': x,
    'y': y,
    'label_to_int': label_to_int,
    'int_to_label':int_to_label
}

# LDA模型
lda = LatentDirichletAllocation(
    n_components =100,
    learning_offset=60.,
    random_state=0,
    learning_method='batch'
    )
docres = lda.fit_transform(tfidf_Tf)


# KNN推荐

import numpy as np

def knn(vec_in, train_feat, train_labels, N):
    '''
    vec_in:
        输入的特征
    train_feat：
        待推荐的所有对象的特征矩阵
    train_labels：
        待推荐的所有对象的标签
    N:
        top N的个数
    '''
    train_featSize = train_feat.shape[0]
    # the distance is defined as: mean(abs(x-mu))
    distances = np.mean(np.abs(
                    np.array(np.tile(vec_in, (train_featSize,1))) - train_feat), 
                    axis = 1)
    # keep the first k items
    sorted_distances_indexes = np.array(distances.argsort())[:N]
    voteIlabels = train_labels[sorted_distances_indexes]
   
    return voteIlabels
