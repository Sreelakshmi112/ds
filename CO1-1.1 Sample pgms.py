#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#sum of 2 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("sum is : " ,a+b)


# In[ ]:


#reverse of a number
num=int(input("Enter the number:" ))
s=0
while num != 0:
 r=num % 10
 s=s * 10 + r
 num= num//10
print("Reversed number is: ",s)


# In[ ]:


#positve or negative number
num=int(input("Enter the number: "))
if(num>0):
  print(num," is positive")
else:
  print(num, "is negative")


# In[ ]:


#count the digits
num=int(input("Enter the number: "))
t=num
count=0
while num>0:
  count=count+1
  num=num//10
print("Number of digits in ",t,"are: ",count)


# In[ ]:


#palindrome
num=int(input("Enter the number:" ))
t=num
s=0
while num != 0:
 r=num % 10
 s=s * 10 + r
 num= num//10
if(t==s):
 print(t," is palindrome.")
else:
  print(t,"is not palindrome.")


# In[ ]:


#area and perimeter of circle
pi=3.14
r=int(input("Enter the radius of the circle: "))
print("Area is :",pi*r*r)
print("perimeter is:",2*pi*r)


# In[ ]:


#biggest of 3 numbers
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if(a>b and a>c):
  print(a," is greater.")
elif(b>c and b>a):
  print(b," is greater.")
else:
  print(c," is greater.")


# In[ ]:


#list and tuple
values = input("Enter comma seprated numbers : ")
list = values.split(",")
print('List : ',list)
tuple1 = tuple(list)
print('Tuple : ',tuple1)


# In[ ]:


#first and last element of a list
list=[1,2,3,4,5]
print("The list is:",list)
print("The first element is: ",list[0]," and last element is:",list[-1])


# In[ ]:


#dictionary
dict={1:'one',2:'two',3:'three',4:'four',5:'five'}
print(dict)


# In[ ]:


#merge two dictionary
dict1={1:'Apple',2:'Mango'}
dict2={3:'Banana',4:'pear'}
print("First dictionary",dict1)
dict1.update(dict2)
print("Second dictionary",dict2)
print("dictionary after merging:",dict1)

