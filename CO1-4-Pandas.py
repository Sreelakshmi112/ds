#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import module pandas
import pandas as pd


# In[2]:



#print a series
a=['a','b','c','d']
s=pd.Series(a)
print(s)


# In[3]:


#print series with index
a=['Apple','Banana','Cat']
s=pd.Series(a,index=['A','B','C'])
print(s)


# In[4]:


#locating value in series using index
a=['Apple','Banana','Cat']
s=pd.Series(a,index=['A','B','C'])
print(s['A'])


# In[5]:


#series using dictionary
dict={'A':'Apple','B':'Ball','C':'Cat'}
s=pd.Series(dict)
print(s)


# In[6]:


#multiples of 2 and 3
a = [i
     for i in range (31)
       if (i % 3 == 0) and (i % 2 == 0)]
s=pd.Series(a)
print(s[1:])


# In[7]:


#Course and number of students using series
a=['30','55','20']
s=pd.Series(a,index=['MCA','MTech','BTech'])
print(s)


# In[8]:


#Course and number of students using dataframe
data = {"Batch": ['MCA', 'BCA', 'BTech'], "Number of Students": [50, 40, 45]}
d=pd.DataFrame(data,index=['B1','B2','B3'])
print(d)


# In[9]:


#Details of 5 students using dataframe
data = {"Name": ['Ayesha', 'Sree', 'Praveena','Sam','Eve'],
         "Percentage": [80, 90, 95,55,75],
         "Grade":['B','A','A','D','C']}
d=pd.DataFrame(data)
print(d)


# In[14]:


df.dropna()


# In[11]:


#Details of 5 students using dataframe WITH INDEX NAME
data = {"Percentage": [80, 90, 95,55,75],
         "Grade":['B','A','A','D','C']}
d=pd.DataFrame(data,index=['Ayesha', 'Sree', 'Praveena','Sam','Eve'])
print(d)


# In[13]:


df=pd.read_csv('C:/Users/Admin/Downloads/marks.csv')
print(df)


# In[ ]:


#loc function
print(d.loc[[2,3]])


# In[17]:


import csv
with open('C:/Users/Admin/Downloads/marks.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)


# In[ ]:


df = pd.read_csv ('std1.csv')
# print(df)
dup = df.duplicated()
print(dup)


# In[ ]:


df = pd.read_csv ('std1.csv')
dup=df.drop_duplicates()
print(dup)


# In[ ]:


df.head(3)


# In[ ]:


df.tail(2)


# In[ ]:


df.corr()


# In[ ]:


import numpy as np
import pandas as pd
array1 = np.array([1,2,3,4])
series3 = pd.Series(array1)
print("Serires :",series3)
print("Array :",array1)

