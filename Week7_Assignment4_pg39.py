#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


location = 'C:\\Users\\nchin\\Data Viz\\Week7_files\\gradedata.csv'


# In[7]:


grade_data = pd.read_csv(location)


# In[8]:


grade_data.head()


# In[9]:


#Create a column indicated whether students are failing or not


# In[10]:


import numpy as np


# In[11]:


grade_data['isFailing'] = np.where(grade_data['grade']<70, 'yes','no')


# In[12]:


grade_data.tail(10)


# In[13]:


#Column seeing how busy a student is


# In[14]:


grade_data['timemgmt'] = np.where((grade_data['exercise']>3)
                                 &(grade_data['hours'] > 17), 'busy', 'not busy')


# In[15]:


grade_data.head(10)


# In[ ]:




