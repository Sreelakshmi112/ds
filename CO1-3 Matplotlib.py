#!/usr/bin/env python
# coding: utf-8

# In[1]:


""""
1. Draw a line in a diagram from position (1, 3) to (2, 10) then to (6, 12) and finally to position 
(18, 20). (Mark each point with a beautiful green colour and set line colour to red and line style 
dotted)
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 18])
ypoints = np.array([3, 10, 12, 20])

plt.plot(xpoints, ypoints,marker = 'o',color="red",mec = 'g', mfc = 'g',linestyle = 'dotted')
plt.show()


# In[2]:


"""
2. Draw a plot for the following data:
Temperature in degree Celsius ,  Sales
        12                       100
        14                       200
        16                       250
        18                       400
        20                       300
        22                       450
        24                       500
"""
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([12,14,16,18,20,22,24])
ypoints = np.array([100,200,250,400,300,450,500])
plt.plot(xpoints, ypoints,marker = 'o',color="red",mec = 'g', mfc = 'g',linestyle = 'dotted')
plt.show()


# In[10]:


"""
4 Write a Python program to plot two or more lines on same plot
  with suitable legends of each line
"""
import matplotlib.pyplot as plt
x1 = [10,20,30]
y1 = [10,20,30]
plt.plot(x1, y1, label = "line 1")
x2 = [30,40,50]
y2 = [30,40,50]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Two Line plot')
plt.legend()
plt.show()


# In[11]:


# Write a Python program to create multiple plots.
import matplotlib.pyplot as plt
figure, axis = plt.subplots(2,2)
x1 = [10,20,30]
y1 = [10,20,30]
axis[0, 0].plot(x1, y1)
axis[0, 0].set_title("Plot 1")
x2 = [10,10,10]
y2 = [30,40,50]
axis[0, 1].plot(x2, y2)
axis[0, 1].set_title("Plot 2")
plt.show()


# In[12]:


"""
6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           7.7  6.7
(i) Write a Python programming to display a bar chart of the popularity of programming Languages.
"""
import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(courses, values, color ='maroon',width = 0.4)
plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()


# In[13]:


""""
6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           7.7  6.7
(ii) Write a Python programming to display a horizontal bar chart
of the popularity of programming 
Languages(Give Red colour to the bar chart).
"""
import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}
courses = list(data.keys())
values = list(data.values())
#fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.barh(courses, values, color ='red')
plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()


# In[14]:


"""
6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           7.7  6.7
(iii) Write a Python programming to display a bar chart of the
      popularity of programming Languages. 
      Use different color for each bar.
"""
import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}
color=("red","yellow","maroon","green","black","cyan")
courses = list(data.keys())
values = list(data.values())
#fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(courses, values, color =color)
plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()


# In[15]:


"""
7. Write a Python program to create bar plot of
scores by group and gender. Use multiple X values on 
the same chart for men and women.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29)
"""
import numpy as np
import matplotlib.pyplot as plt
y1 = [22,30,35,35,26]
y2 = [25,32,30,35,29]
x_labels = ['G1','G2','G3','G4','G5']
x1 = np.arange(5)
width = 0.40
plt.bar(x1-0.2,y1,color="green",width=width,label='Men')
plt.bar(x1+0.2,y2,color="red",width=width,label='Women')
plt.xticks(x1,x_labels)
plt.xlabel("Person")
plt.ylabel("Scores")
plt.legend()
plt.title("scores by group and gender")
plt.show()


# In[16]:


"""
8. Write a Python programming to create a pie chart
   of the popularity of programming Languages.
   
Programming languages: Java Python PHP JavaScript C# C++
Popularity           : 22.2 17.6   8.8 8          7.7 6.7
"""
import matplotlib.pyplot as plt
import numpy as np
y = np.array([22.2,17.6,8.8,8,7.7,6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
plt.pie(y, labels = mylabels)
plt.show() 


# In[25]:


"""
9. Write a Python programming to create a pie chart of
gold medal achievements of five most 
successful countries in 2016 Summer Olympics.
Read the data from a csv file.
Sample data:medal.csv
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19
Germany,17
"""

import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('C:/Users/Admin/Downloads/medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
plt.pie(medal_data, labels=country_data)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show() 


# In[18]:


"""
10. Write a Python program to draw a scatter plot comparing two subject
marks of Mathematics and Science. Use marks of 10 students.
Sample data:
Test Data:
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""
import matplotlib.pyplot as plt
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
m = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
s = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
plt.scatter(x, m,label="maths marks")
plt.scatter(x, s,label="science marks")
plt.legend(loc='upper right')
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter plot")
plt.show() 


# In[ ]:




