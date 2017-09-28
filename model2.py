import pandas as pd
from pandas.io import gbq

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Get the data from BigQuery
query = """SELECT * FROM [ziggo-big-query:Menno.pr_train] LIMIT 10"""
pid = 'ziggo-big-query'

data = gbq.read_gbq(query,project_id=pid)

# Define datasets
X=data[:,4:8]
Y=data[:,3]

seed=111
test_size = 0.2
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=test_size,random_state=seed)

# Fit a model
xg_train = xgb.DMatrix(X_train,label=y_train)
xg_test = xgb.DMatrix(X_test,label=y_test)

param = {}
param['objective'] = 'multi:softmax'
param['eta'] = 0.05
param['max_depth'] = 6
param['silent'] = 1
param['num_class'] = 3

watchlist = [(xg_train,'train'),(xg_test,'test')]
num_round = 100
bst = xgb.train(param,xg_train,num_round,watchlist)

# Accuracies 
y_pred = bst.predict(xg_test)
y_last = X_test[:,0]

acc1 = accuracy_score(y_test,y_pred)
acc2 = accuracy_score(y_test,y_last)

print(acc1)
print(acc2)





