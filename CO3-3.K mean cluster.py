#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


# In[2]:


iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target


# In[3]:


plt.scatter(X[:,0], X[:,1], c=y, cmap='prism')
plt.xlabel('Spea1 Length', fontsize=18)
plt.ylabel('Sepal Width', fontsize=18)


# In[4]:


km = KMeans(n_clusters = 3, init='k-means++', n_init=10, max_iter=300, tol=0.0001, verbose=0, random_state=21, copy_x=True, algorithm="auto")
km.fit(X)
centers = km.cluster_centers_
print(centers)
new_labels = km.labels_
print(new_labels)
print(y)


# In[5]:


fig, axes = plt.subplots( 1,2, figsize=(16,8))
axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='prism',edgecolor='k', s=75)
axes[1].scatter(X[:, 0], X[:, 1], c=new_labels, cmap='jet',edgecolor='k', s=75)
axes[0].set_xlabel('Sepal length', fontsize=12)
axes[0].set_ylabel('Sepal width', fontsize=12)
axes[1].set_xlabel('Sepal length', fontsize=12)
axes[1].set_ylabel('Sepal width', fontsize=12)
axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=15)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=15)
axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('Predicted', fontsize=18)


# In[6]:


km = KMeans(n_clusters = 3, init='k-means++', n_init=10, max_iter=300, tol=0.0001, verbose=0, random_state=21, copy_x=True, algorithm="auto")
km.fit(X)
km.fit_predict(X)
km.fit_transform(X)
km.get_params()
km.predict(X)
km.score(X)
km.transform(X)

