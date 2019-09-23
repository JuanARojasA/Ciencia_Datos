#!/usr/bin/env python
# coding: utf-8

# 1) Importar el Data Set “Resultados Saber Pro Competencias Especificas 2018-2” de
# Datos Abiertos.

# In[15]:


import pandas as pd

saberPro = pd.read_csv("https://www.datos.gov.co/api/views/u7fi-34mq/rows.csv?accessType=DOWNLOAD")

saberPro


# 2) Imprimir los consecutivos de los estudiantes que en la prueba de GESTIÓN
# FINANCIERA obtuvieron un DESEMPEÑO superior a 2

# In[16]:


saberPro['ESTU_CONSECUTIVO'][(saberPro['RESULT_NOMBREPRUEBA'] == 'GESTIÓN FINANCIERA') & (saberPro['RESULT_DESEMPENO'] >=2)]


# 3) Imprimir los CONSECUTIVOS de los estudiantes que en la prueba de FORMULACIÓN
# DE PROYECTOS DE INGENIERÍA obtuvieron un PUNTAJE inferior a 170

# In[17]:


saberPro['ESTU_CONSECUTIVO'][(saberPro['RESULT_NOMBREPRUEBA'] == 'FORMULACIÓN DE PROYECTOS DE INGENIERÍA') & (saberPro['RESULT_PUNTAJE'] <=170)]


# 4) Imprima los CONSECUTIVOS de los estudiantes y el NOMBRE DE LA PRUEBA donde
# el PUNTAJE sea superior a 200

# In[18]:


saberPro.loc[saberPro['RESULT_PUNTAJE'] >=200, ['ESTU_CONSECUTIVO','RESULT_NOMBREPRUEBA']]


# 5) Imprima el NOMBRE DE LAS PRUEBAS que obtuvieron DESEMPEÑO superior a 3 (Ojo el nombre de las pruebas no puede estar repetido)

# In[19]:


pruebas = saberPro.drop_duplicates(subset=['RESULT_NOMBREPRUEBA'], keep='first')
pruebas['RESULT_NOMBREPRUEBA'][pruebas['RESULT_DESEMPENO'] >=3]


# 6) Utilizando WHERE convierta en NaN todos los registros donde el PUNTAJE no sea
# superior a 170 y luego elimine esos registros.

# In[24]:


puntaje = saberPro.where(saberPro['RESULT_PUNTAJE']>=170, inplace=False)
puntaje.dropna(axis=0, how='any')


# 7) Utilizando MASK convierta en NaN todos los registros donde el DESEMPEÑO no sea
# inferior a 3 y luego elimine esos registros.

# In[30]:


desempeno = saberPro.mask(saberPro['RESULT_DESEMPENO']>3)
desempeno.dropna(axis=0, how='any')


# 8) Utilizando Isin imprima los CONSECUTIVOS de los estudiantes y el NOMBRE
# DE LA PRUEBA donde el PUNTAJE sea 160 o 170 o 180 o 190 o 200.

# In[38]:


saberPro.loc[saberPro['RESULT_PUNTAJE'].isin([160,170,180,190,200]), ['ESTU_CONSECUTIVO','RESULT_NOMBREPRUEBA']]


# In[ ]:




