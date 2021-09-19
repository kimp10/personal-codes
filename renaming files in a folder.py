#!/usr/bin/env python
# coding: utf-8

# In[2]:



# Python program to rename all file
# names in your directory 
import os
  
os.chdir(r'C:\Users\Khutso Mpelo\Documents\hr analytics\wetransfer-c412b6-20210720T184202Z-001\wetransfer-c412b6')
print(os.getcwd())
COUNT = 100
  
# Function to increment count 
# to make the files sorted.
def increment():
    global COUNT
    COUNT = COUNT + 1
  
  
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = str(COUNT)
    increment()
  
    new_name = '{}{}'.format(f_name, f_ext)
    os.rename(f, new_name)


# In[ ]:




