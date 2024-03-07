#!/usr/bin/env python
# coding: utf-8

# In[2]:


# write a program to check a number is prime or not
number = int(input("Enter any number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

    


# In[ ]:




