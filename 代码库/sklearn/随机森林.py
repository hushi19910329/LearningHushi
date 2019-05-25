# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:13:45 2019

@author: 绿逗先生
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import  metrics

#加载数据
data= np.loadtxt('E:/python/数据2.txt', delimiter=",",usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12))#一列标签+12个特征
#print(data)
x,y = data[:,1:13],data[:,0]#选取列
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)#划分数据集
#train= np.column_stack((X_train,y_train))
#np.savetxt('train_usual.csv',train, delimiter = ',')
#test = np.column_stack((x_test, y_test))

#1.首先，不管任何参数，都选择默认，我们先拟合下数据看看：
rf0 = RandomForestClassifier(oob_score=True, random_state=12)
rf0.fit(x_train,y_train.astype('int'))
print (rf0.oob_score_)
y_predprob = rf0.predict_proba(x_test)[:,1]
print( "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob))
#拟合效果rf0.oob_score_=0.9737888198757764
#RF的默认参数拟合效果在本例比较好一些。
#AUC（Area under the Curve of ROC）Score (Train): 1.000000


#2.我们首先对n_estimators进行网格搜索：
param_test1 = {'n_estimators':[50,120,160,200,250]}
gsearch1 = GridSearchCV(estimator = RandomForestClassifier(min_samples_split=100,
                                  min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10), 
                       param_grid = param_test1, scoring='roc_auc',cv=5)
gsearch1.fit(x_train,y_train)
print( gsearch1.best_params_, gsearch1.best_score_)#,gsearch1.cv_results_打印拟合结果)
#这样我们得到了最佳的弱学习器迭代次数50
#提供优化过程期间观察到的最好的评分gsearch1.best_score_=1

#3.接着我们对决策树最大深度max_depth和内部节点再划分所需最小样本数min_samples_split进行网格搜索。
param_test2 = {'max_depth':[1,2,3,5,7,9,11,13]}#, 'min_samples_split':[100,120,150,180,200,300]}
gsearch2 = GridSearchCV(
    estimator = RandomForestClassifier(n_estimators=50, min_samples_split=100,
  min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10),
    param_grid = param_test2, scoring='roc_auc',iid=False, cv=5)
gsearch2.fit(x_train,y_train)
print( gsearch2.best_params_, gsearch2.best_score_)

#得到最佳 max_depth = 2
#我们看看我们现在模型的袋外分数：

rf1 = RandomForestClassifier(n_estimators= 50, max_depth=2, min_samples_split=100, min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10)
rf1.fit(x_train,y_train)
print( rf1.oob_score_)
y_predprob = rf1.predict_proba(x_test)[:,1]
print( "AUC Score (Train): %f" % metrics.roc_auc_score(y_test, y_predprob))
#输出结果为0.9841897233201581
#相对于默认情况,袋外分数有提高，也就是说模型的泛化能力变好了
#对于内部节点再划分所需最小样本数min_samples_split，我们暂时不能一起定下来，因为这个还和决策树其他的参数存在关联。

#4.下面我们再对内部节点再划分所需最小样本数min_samples_split和叶子节点最少样本数min_samples_leaf一起调参。
param_test3 = {'min_samples_split':[80,100,120,140], 'min_samples_leaf':[10,20,30,40,50,100]}
gsearch3 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 50, max_depth=2,
                                  max_features='sqrt' ,oob_score=True, random_state=10),
param_grid = param_test3, scoring='roc_auc',iid=False, cv=5)
gsearch3.fit(x_train,y_train)
print( gsearch3.best_params_, gsearch3.best_score_)
#得到最佳'min_samples_leaf': 10, 'min_samples_split': 80

#5.最后我们再对最大特征数max_features做调参:
param_test4 = {'max_features':[3,5,7,9,11]}
gsearch4 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 50, max_depth=2, min_samples_split=80,
                                  min_samples_leaf=10 ,oob_score=True, random_state=10),
   param_grid = param_test4, scoring='roc_auc',iid=False, cv=5)
gsearch4.fit(x_train,y_train)
print( gsearch4.best_params_, gsearch4.best_score_)
#得到'max_features': 3

#6.用我们搜索到的最佳参数，我们再看看最终的模型拟合：
rf2 = RandomForestClassifier(n_estimators= 50, max_depth=2, min_samples_split=80,
                                min_samples_leaf=10,max_features=3,oob_score=True, random_state=10)
rf2.fit(x_train,y_train)
print (rf2.oob_score_)
#此时的输出为：0.99
#可见此时模型已经最优化
