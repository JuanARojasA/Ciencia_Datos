#!/usr/bin/env python
# coding: utf-8

# 1. Cargar el CSV phone_data y convertir la columna date de string a tiempo

# In[1]:


import pandas as pd
import dateutil


# In[7]:


data = pd.read_csv('phone_data.csv')
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)
data


# 3. ¿Cuál fue el ítem (llamada/datos) de mayor duración?

# In[8]:


data['duration'].max()


# 4. ¿Cuál fue la llamada de mayor duración?

# In[14]:


data['duration'][(data['item'] == 'call')].max()


# 5. ¿Cuál fue el evento de datos de mayor duración?

# In[15]:


data['duration'][(data['item'] == 'data')].max()


# 6. ¿Cuánto fue el total de segundos de todas las llamadas?

# In[16]:


data['duration'][data['item'] == 'call'].sum()


# 7. ¿Cuánto fue el total de segundos entre sms y eventos de datos?

# In[20]:


data['duration'][data['item'] == 'sms'].sum() + data['duration'][data['item'] == 'data'].sum()


# 8. ¿Cuántas entradas hay por cada uno de los meses?

# In[21]:


data['month'].value_counts()


# 9. ¿Cuántas entradas de datos haypor cada una delas redes?

# In[22]:


data['network'][data['item'] == 'data'].value_counts()


# 10. ¿Cuántas entradas de llamada hay por cada una de las redes?

# In[23]:


data['network'][data['item'] == 'call'].value_counts()


# 11. Obtener la suma de la duración por mes 

# In[24]:


data.groupby('month')['duration'].sum()


# 12. Obtener el promedio de llamadas por cada una de las redes

# In[39]:


data[data['item'] == 'call'].groupby('network')['duration'].mean()


# 13. Obtener el promedio de eventos de datos por cada una de las redes

# In[40]:


data[data['item'] == 'data'].groupby('network')['duration'].mean()


# 14. Obtener el número de entradas por mes

# In[41]:


data.groupby('month')['date'].count()


# 15. Obtener el número de entradas de tipo llamada por cada una de las redes

# In[43]:


data[data['item'] == 'call'].groupby('network')['duration'].count()


# 16. Obtener el número de entradas tipo sms para cada una de las redes

# In[44]:


data[data['item'] == 'sms'].groupby('network')['duration'].count()


# 17. ¿Cuántos eventos de llamada, datos y sms hubo por mes?

# In[45]:


data.groupby(['month', 'item'])['date'].count()


# 18. Por cada uno de los meses, ¿Cuántas veces se usaron cada una de las redes (para cualquier evento)?

# In[46]:


data.groupby(['month', 'network'])['date'].count()


# 19. Por cada uno de los meses, ¿Cuántas veces se usaron cada una de las redes, discriminando el tipo de evento?

# In[48]:


data.groupby(['month', 'network','item'])['date'].count()

