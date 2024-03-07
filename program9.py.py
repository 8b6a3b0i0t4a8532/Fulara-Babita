#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a program to count occurance of each element in the list
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x)))


# In[ ]:




