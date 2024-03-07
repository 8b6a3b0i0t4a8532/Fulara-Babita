#!/usr/bin/env python
# coding: utf-8

# In[2]:


# write a program to read data from CSV file and display first five rows and last five rows
import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("First 5 rows:")
print(diamonds.head())


# In[ ]:




