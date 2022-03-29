#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# In[2]:


data=load_iris()
x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2)


# In[3]:


dt=tree.DecisionTreeClassifier()
dt.fit(x_train,y_train)
tree.plot_tree(dt)


# In[4]:


y_predict=dt.predict(x_test)
print(y_predict)
accuracy_score(y_test,y_predict)

