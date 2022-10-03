#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Swaping of numbers

#first method
p=input("declare first number")
q=input("declare second number") 
print ("first number is :", q) 
print ("second number is : " , p)

#second method

p=int(input("declare First number="))
q=int(input("declare Second Number=")) 
p=p+q
q=p-q
p=p-q 
print("first number is : " ,p)
print ("second number is : " , q)


# In[15]:


#Factorial
a=int(input("enter a number:"))   
factorial=1 
if a<0:
    print("factorial doen not exist")
else:
    for i in range(1, a+1):
        factorial=factorial* i 
        
print ("The factorial of" , a, "is : " , factorial)


# In[16]:


#Fibonacci Series
limit=int(input("enter a limit:"))
n1=0
n2=1
i=0
if limit<0:
    print("negative numbers are not allowed")
else:
    print("Fibonacci series upto", limit, "is:")
    while i<limit:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        i+=1


# In[23]:


# String Commands
 #len
a="my name is Iqra"
print(a)
print("the length of a is:", len(a))

#substring
a="slicing the string"
print(a[0:7])
print(a[8:11])
print(a[-6:-1])

#concatination
a="Joining"
b="two or more"
c="strings"
d=a+" "+b+ " "+c
print(d)


# In[26]:


#Calculator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
opr=int(input("select operation: enter 1 for addition, 2 for subtraction, 3 for multiplication or 4 for division : "))

if opr==1:
    c=a+b
    print(a,"+", b, "=" ,c)
elif opr==2:
    c=a-b
    print(a, "-", b ,"=", c)
elif opr==3:
    c=a*b
    print(a, "*", b, "=", c)
elif opr==4:
    c=a/b
    print(a, "/", b, "=" ,c)
else:
    print("invalid operation")


# In[ ]:




