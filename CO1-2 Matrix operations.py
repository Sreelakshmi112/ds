#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
  
# initializing matrices
x = numpy.array([[1, 2], [3, 4]])
y = numpy.array([[5, 6], [7, 8]])
print("Given matrix:")
print(x)
# using multiply() to multiply matrices element wise
print ("The element wise multiplication of matrix is : ")
print (numpy.multiply(x,y))
# using dot() to multiply matrices
print ("The product of matrices is : ")
print (numpy.dot(x,y))
# using "T" to transpose the matrix
print ("The transpose of given matrix is : ")
print (x.T)
# using "trace" to find trace of the matrix
print ("The trace of given matrix is : ")
print (x.trace())
#Rank of matrix
print(numpy.linalg.matrix_rank(x))
#Determinant of matrix
print(numpy.linalg.det(x))
#Inverse of matrix
print(numpy.linalg.inv(x))
#Eigen values of matrix
print(numpy.linalg.eig(x))


# In[2]:


import numpy as py
a=py.array([[2,4,5],[1,2,3],[4,3,2]])
u,d,vt=py.linalg.svd(a)
ar=(u@py.diag(d)@vt)
print(u)
print(d)
print(vt)
print(ar)


# In[ ]:




