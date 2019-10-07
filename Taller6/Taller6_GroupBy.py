#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import dateutil


# In[7]:


data = pd.read_csv('phone_data.csv')
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)
data


# In[8]:


data['duration'].max()


# In[14]:


data['duration'][(data['item'] == 'call')].max()


# In[15]:


data['duration'][(data['item'] == 'data')].max()


# In[16]:


data['duration'][data['item'] == 'call'].sum()


# In[20]:


data['duration'][data['item'] == 'sms'].sum() + data['duration'][data['item'] == 'data'].sum()


# In[21]:


data['month'].value_counts()


# In[22]:


data['network'][data['item'] == 'data'].value_counts()


# In[23]:


data['network'][data['item'] == 'call'].value_counts()


# In[24]:


data.groupby('month')['duration'].sum()


# In[39]:


data[data['item'] == 'call'].groupby('network')['duration'].mean()


# In[40]:


data[data['item'] == 'data'].groupby('network')['duration'].mean()


# In[41]:


data.groupby('month')['date'].count()


# In[43]:


data[data['item'] == 'call'].groupby('network')['duration'].count()


# In[44]:


data[data['item'] == 'sms'].groupby('network')['duration'].count()


# In[45]:


data.groupby(['month', 'item'])['date'].count()


# In[46]:


data.groupby(['month', 'network'])['date'].count()


# In[48]:


data.groupby(['month', 'network','item'])['date'].count()


# In[ ]:




