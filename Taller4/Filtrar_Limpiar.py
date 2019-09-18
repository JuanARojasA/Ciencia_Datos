#!/usr/bin/env python
# coding: utf-8

# $Importar\ CSV\$

# In[1]:


import pandas as pd

docentes = pd.read_csv("https://www.datos.gov.co/api/views/e2ws-b9ku/rows.csv?accessType=DOWNLOAD")

docentes


# $Limpiar\ Datos\$

# Retorna una matriz con valores True o False

# In[2]:


docentes_nan = docentes.isnull() #Devuelve una matriz con valores True False
print(docentes_nan)


# Limpia las filas donde exista al menos NAN

# In[3]:


docentes_sin_nan1 = docentes.dropna(axis=0, how='any')
print(docentes_sin_nan1)


# Limpia las filas donde todos sus valores sean NAN

# In[4]:


docentes_sin_nan2 = docentes.dropna(axis=0, how='all')
print(docentes_sin_nan2)


# Limpia las columnas donde exista al menos un NAN

# In[5]:


docentes_sin_nan3 = docentes.dropna(axis=1, how='any')
print(docentes_sin_nan3)


# Llena todos los NAN con '3'

# In[6]:


docentes_nuevo = docentes.fillna(value=3)
print(docentes_nuevo)


# Donde exista un NAN lo cambiará por el valor medio de dicha columna

# In[7]:


docentes_nuevo = docentes.fillna(docentes.mean())
print(docentes_nuevo)


# Completa los NAN utilizando el valor de la fila i+1, en la misma columna

# In[8]:


docentes_nuevo = docentes.fillna(method='bfill', limit=1)
print(docentes_nuevo)


# Retorna una serie con el resultado de evaluar la condición de que la celda de la columna 'DOCTORADO' sea ">=5"

# In[9]:


docentes['DOCTORADO'] >= 5


# Retorna un DataFrame con unicamente las filas donde su columna 'DOCTORADO'  satisfaga que el valor sea ">=5"

# In[10]:


docentes[docentes['DOCTORADO'] >=5]


# Retorna La Columna "Programas Académicos" donde su valor de 'DOCTORADO' sea ">=5"

# In[11]:


docentes['Programa Académico'][docentes['DOCTORADO'] >=5]


# Retorna un DataFrame con unicamente las filas en donde se cumplan las condiciones de que su 'DOCTORADO' sea ">=5" y a su vez la 'MAESTRÍA" sea ">=7"

# In[12]:


docentes[(docentes['DOCTORADO'] >=5) & (docentes['MAESTRÍA'] >=7)]


# Las filas en donde no se cumpla con la condición de que la 'ESPECIALIZACIÓN' sea ">=2" se llenarán de NaN

# In[21]:


docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.where(docentes_n2['ESPECIALIZACIÓN']>=2)


# Las filas en donde se cumpla con la condición de que la 'ESPECIALIZACIÓN' sea ">=2" se llenarán de NaN

# In[22]:


docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.mask(docentes_n2['ESPECIALIZACIÓN']>=2)


# Retorna un DataFrame con valores True o False, evaluando si el valor de cada celda se encuentra en la lista "[5,8,10,12,14]"

# In[27]:


docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.isin([5,8,10,12,14])


# Retorna un DataFrame con las filas donde se cumpla la condición de que el valor de la columna 'DOCTORADO' sea mayor al de la celda 'MAESTRÍA'

# In[28]:


docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.query('DOCTORADO > MAESTRÍA')


# Devuelve una Serie con la evaluación de la operación 'DOCTORADO+MAESTRÍA'

# In[30]:


docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.eval('DOCTORADO + MAESTRÍA')


# In[ ]:




