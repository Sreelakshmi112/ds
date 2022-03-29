#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
linreg = LinearRegression()
linreg.fit(X, y)
y_pred = linreg.predict(X)
print(y_pred)
linreg.score(X,y)
import matplotlib.pyplot as plt
plt.plot(X,y)

