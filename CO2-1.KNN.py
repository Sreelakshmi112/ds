#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# In[2]:


data=load_iris()


# In[3]:


x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2)


# In[4]:


knn=KNeighborsClassifier()


# In[5]:


knn.fit(x_train,y_train)


# In[10]:


y_pred=knn.predict(x_test)
print(y_pred)


# In[11]:


knn.predict_proba(x_test)


# In[12]:


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

