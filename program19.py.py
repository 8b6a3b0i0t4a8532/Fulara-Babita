#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a program to print ASCII value of the character
print("enter a string:",end="")
text = input()
textlengthn = len(text)
for char in text:
    ascii = ord(char)
    print(char,"\t",ascii)


# In[ ]:




