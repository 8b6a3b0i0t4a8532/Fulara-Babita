#!/usr/bin/env python
# coding: utf-8

# In[23]:


s = [2,3,3,6,4,6,9]
mn=s[0]
mx=s[0]

for i in s:
    if mx<i:
        mx=i
    if mn>i:
        mn=i
        
 
print ("max : " ,mx)
print ("min : " ,mn)   


# In[ ]:




