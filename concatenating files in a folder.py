#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import glob
import os


# In[10]:


path = r'C:\Users\Khutso Mpelo\Documents\Adobe\coding_test\coding_test\data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df['file_name'] = filename
    li.append(df)

df_all = pd.concat(li, axis=0, ignore_index=True)

