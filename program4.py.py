#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a program to demonstrate list,set,tuple,dictionary

# Lists
l = []
 
# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)
 
# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()
 
# Set
s = set()
 
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
 
# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()
 
# Tuple
t = tuple(l)
 
# Tuples are immutable
print("Tuple", t)
print()
 
# Dictionary
d = {}
 
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)
 
# Removing key-value pair
del d[10]
print("Dictionary", d)


# In[ ]:




