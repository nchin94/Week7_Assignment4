#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


names = ['Jan','John','Bob','Jan','Mary','Jon','Mel','Mel']
grades = [95,78,76,95,77,78,99,100]


# In[3]:


GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades']) 


# In[4]:


df


# In[6]:


bins = [0,60,70,80,90,100]
group_names = ['F','D','C','B','A']


# In[11]:


df['Letter_Grade'] = pd.cut(df['Grades'], bins, labels = group_names)


# In[12]:


df


# In[ ]:


#pass or fail


# In[13]:


MasterBin = [0,80,100]
MasterGroupNames = ['Fail', 'Pass']


# In[14]:


df['PassOrFail'] = pd.cut(df['Grades'], MasterBin, labels = MasterGroupNames)


# In[15]:


df


# In[ ]:




