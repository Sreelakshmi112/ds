#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
iris=load_iris()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=1) 
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(6,),random_state=1)
clf.fit(x_train,y_train)     
clf.score(x_train,y_train)  
y_pred=clf.predict(x_test)
print(y_pred)
from sklearn.metrics import accuracy_score
print("accuracy score:",accuracy_score(y_test,y_pred))

