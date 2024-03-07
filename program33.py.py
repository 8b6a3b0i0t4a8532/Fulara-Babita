#!/usr/bin/env python
# coding: utf-8

# In[3]:


# write a program to check given mobile number is valid or not

import re
 
def isValid(s):
     
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(s)
 
s = "8630498582"
if (isValid(s)): 
    print ("Valid Number")     
else :
    print ("Invalid Number") 
 

