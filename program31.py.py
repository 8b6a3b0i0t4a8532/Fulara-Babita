#!/usr/bin/env python
# coding: utf-8

# In[4]:


# write a program to find mean,variance and standard deviation of the list using numpy
import numpy as np 
array = np.arange(10) 
print(array) 
  
r1 = np.mean(array) 
print("\nMean: ", r1) 
  
r2 = np.std(array) 
print("\nstd: ", r2) 
  
r3 = np.var(array) 
print("\nvariance: ", r3) 


# In[ ]:




