#!/usr/bin/env python
# coding: utf-8

# In[4]:


#write a program to check a number is armstrong or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[ ]:




