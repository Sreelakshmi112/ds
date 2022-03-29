#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
df = datasets.load_iris()
df['feature_names']
x,y=datasets.load_iris(return_X_y=True)
x.shape
y.shape
x=x[:, np.newaxis, 2]
x.shape
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 1/3, random_state=0)  
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
pred=regr.predict(x_test)
print("Coefficients: \n", regr.coef_)
print("Mean squared error: %.2f" % mean_squared_error(y_test,pred))
print("Coefficient of determination: %.2f" % r2_score(y_test,pred))
plt.scatter(x_test,y_test, color="black")
plt.plot(x_test,pred, color="blue", linewidth=3)
plt.xlabel("sepal length")
plt.ylabel("flower category")
plt.xticks(())
plt.yticks(())
plt.show()

