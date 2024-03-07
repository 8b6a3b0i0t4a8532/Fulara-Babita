#!/usr/bin/env python
# coding: utf-8

# In[3]:


# program to count vowels in a string 
def isVowel(ch): 
    return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 
  
 
def countVowels(str): 
    count = 0
    for i in range(len(str)): 
  
        if isVowel(str[i]): 
            count += 1
    return count 
  
str = 'hello python'

print(countVowels(str)) 
  


# In[ ]:




