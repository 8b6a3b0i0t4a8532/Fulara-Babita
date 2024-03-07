#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a program to display only digitsfrom tuple

import re
List = [(25, 13), (22, 19)]

print("Orignal list : ", List)
temp = re.sub(r'[\[\]\(\), ]', '', str(List))

result =  [int(i) for i in set(temp)]

print("Digits Extracted: ",result)


# In[ ]:




