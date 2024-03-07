#!/usr/bin/env python
# coding: utf-8

# In[2]:


#write a program to find all prime numbers from 1 to n 
def isPrime(n):
    if(n==1 or n==0):
        return False
   
    for i in range(2,(n//2)+1):
        
        if(n%i==0):
            return False
    return True
N = 100;
for i in range(1,N+1):
  if(isPrime(i)):
      print(i,end=" ")


# In[ ]:




