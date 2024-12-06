#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[12]:


df.info()


# In[13]:


df.describe()


# In[15]:


df.isnull().sum()


# In[16]:


df.nunique()


# In[17]:


df.sort_values(by="World Population Percentage",ascending = False).head(10)


# In[18]:


df.corr()


# In[19]:


sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (23,8)
plt.show()


# In[20]:


df.groupby('Continent').mean().sort_values(by = "2022 Population",ascending = False)


# In[28]:


df[df['Continent'].str.contains('Africa')]


# In[29]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by = "2022 Population",ascending = False)
df2


# In[30]:


df3 = df2.transpose()
df3


# In[25]:


df.columns


# In[26]:


df3.plot()


# In[27]:


df.select_dtypes(include ='float')


# In[ ]:




