#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
data=load_iris()
nb=GaussianNB()
x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
nb.fit(x_train,y_train)
y_pred=nb.predict(x_test)
print(y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

