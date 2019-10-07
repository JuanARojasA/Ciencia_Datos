
$Importar\ CSV\$


```python
import pandas as pd

docentes = pd.read_csv("https://www.datos.gov.co/api/views/e2ws-b9ku/rows.csv?accessType=DOWNLOAD")

docentes
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CIENCIAS AGROINDUSTRIALES</td>
      <td>INGENIERIA DE ALIMENTOS</td>
      <td>NaN</td>
      <td>8</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>8</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>TECNOLOGIA AGROINDUSTRIAL</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>TECNOLOGIA AGROPECUARIA</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Total CIENCIAS AGROINDUSTRIALES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11</td>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>11</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>BIOLOGIA</td>
      <td>NaN</td>
      <td>9</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>9</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>FISICA</td>
      <td>NaN</td>
      <td>10</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>10</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>QUIMICA</td>
      <td>NaN</td>
      <td>13</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>3.0</td>
      <td>13</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>13</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>TECNOLOGIA EN INSTRUMENTACION ELECTRONICA</td>
      <td>NaN</td>
      <td>11</td>
      <td>11</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>11</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Total CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43</td>
      <td>43</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>19.0</td>
      <td>43</td>
      <td>6.0</td>
      <td>15.0</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>43</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CIENCIAS DE LA SALUD</td>
      <td>ENFERMERIA</td>
      <td>2.0</td>
      <td>4</td>
      <td>6</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>6</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>6</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>MEDICINA</td>
      <td>27.0</td>
      <td>16</td>
      <td>43</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>43</td>
      <td>18.0</td>
      <td>13.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>43</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>SEGURIDAD Y SALUD EN EL TRABAJO</td>
      <td>NaN</td>
      <td>3</td>
      <td>3</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Total CIENCIAS DE LA SALUD</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>23</td>
      <td>52</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>40.0</td>
      <td>9.0</td>
      <td>52</td>
      <td>23.0</td>
      <td>15.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>52</td>
    </tr>
    <tr>
      <th>13</th>
      <td>CIENCIAS ECONOMICAS Y ADMINISTRATIVAS</td>
      <td>ADMINISTRACION DE NEGOCIOS  PRESENCIAL</td>
      <td>NaN</td>
      <td>3</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>3</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>ADMINISTRACION FINANCIERA</td>
      <td>NaN</td>
      <td>3</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>3</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>CONTADURIA</td>
      <td>NaN</td>
      <td>20</td>
      <td>20</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>20</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>20</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>ECONOMIA</td>
      <td>NaN</td>
      <td>4</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30</td>
      <td>30</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>27.0</td>
      <td>1.0</td>
      <td>30</td>
      <td>4.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>30</td>
    </tr>
    <tr>
      <th>18</th>
      <td>CIENCIAS HUMANAS Y BELLAS ARTES</td>
      <td>ARTES VISUAL</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>CIENCIAS DE LA INFORMACION Y LA DOC</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>COMUNICACION SOCIAL Y PERIODISMO</td>
      <td>NaN</td>
      <td>7</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>7</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>7</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>FILOSOFIA</td>
      <td>NaN</td>
      <td>6</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>6</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>GERONTOLOGIA</td>
      <td>NaN</td>
      <td>3</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>TRABAJO SOCIAL</td>
      <td>NaN</td>
      <td>9</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>9</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Total CIENCIAS HUMANAS Y BELLAS ARTES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28</td>
      <td>28</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19.0</td>
      <td>9.0</td>
      <td>28</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>25</th>
      <td>EDUCACION</td>
      <td>LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...</td>
      <td>NaN</td>
      <td>10</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>10</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NaN</td>
      <td>LICENCIATURA EN EDUCACION FISICA Y DEPORTES   ...</td>
      <td>NaN</td>
      <td>4</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>27</th>
      <td>NaN</td>
      <td>LICENCIATURA EN ESPAÑOL Y LITERATURA          ...</td>
      <td>NaN</td>
      <td>8</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>2.0</td>
      <td>8</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>28</th>
      <td>NaN</td>
      <td>LICENCIATURA EN LENGUAS MODERNAS</td>
      <td>NaN</td>
      <td>12</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>12</td>
      <td>7.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NaN</td>
      <td>LICENCIATURA EN MATEMATICAS</td>
      <td>NaN</td>
      <td>18</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>7.0</td>
      <td>18</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>18</td>
    </tr>
    <tr>
      <th>30</th>
      <td>NaN</td>
      <td>LICENCIATURA EN PEDAGOGIA INFANTIL</td>
      <td>NaN</td>
      <td>7</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Total EDUCACION</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59</td>
      <td>59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.0</td>
      <td>18.0</td>
      <td>59</td>
      <td>8.0</td>
      <td>24.0</td>
      <td>17.0</td>
      <td>10.0</td>
      <td>59</td>
    </tr>
    <tr>
      <th>32</th>
      <td>INGENIERIA</td>
      <td>INGENIERIA CIVIL</td>
      <td>NaN</td>
      <td>17</td>
      <td>17</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>17</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>17</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NaN</td>
      <td>INGENIERIA DE SISTEMAS</td>
      <td>NaN</td>
      <td>15</td>
      <td>15</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>15</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>34</th>
      <td>NaN</td>
      <td>INGENIERIA ELECTRONICA</td>
      <td>NaN</td>
      <td>14</td>
      <td>14</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>14</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>14</td>
    </tr>
    <tr>
      <th>35</th>
      <td>NaN</td>
      <td>TECNOLOGIA EN OBRAS CIVILES</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>36</th>
      <td>NaN</td>
      <td>TECNOLOGIA EN TOPOGRAFIA</td>
      <td>NaN</td>
      <td>8</td>
      <td>8</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>8</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Total INGENIERIA</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55</td>
      <td>55</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>36.0</td>
      <td>12.0</td>
      <td>55</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>55</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Total general</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>249</td>
      <td>278</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>192.0</td>
      <td>73.0</td>
      <td>278</td>
      <td>62.0</td>
      <td>110.0</td>
      <td>64.0</td>
      <td>42.0</td>
      <td>278</td>
    </tr>
  </tbody>
</table>
</div>



$Limpiar\ Datos\$

Retorna una matriz con valores True o False


```python
docentes_nan = docentes.isnull() #Devuelve una matriz con valores True False
print(docentes_nan)
```

        Facultad  Programa Académico     TC     MT  TOTAL  PREGRADO  \
    0      False               False   True  False  False      True   
    1       True               False   True  False  False      True   
    2       True               False   True  False  False      True   
    3      False                True   True  False  False      True   
    4      False               False   True  False  False      True   
    5       True               False   True  False  False      True   
    6       True               False   True  False  False      True   
    7       True               False   True  False  False      True   
    8      False                True   True  False  False      True   
    9      False               False  False  False  False      True   
    10      True               False  False  False  False     False   
    11      True               False   True  False  False      True   
    12     False                True  False  False  False     False   
    13     False               False   True  False  False      True   
    14      True               False   True  False  False      True   
    15      True               False   True  False  False      True   
    16      True               False   True  False  False      True   
    17     False                True   True  False  False      True   
    18     False               False   True  False  False      True   
    19      True               False   True  False  False      True   
    20      True               False   True  False  False      True   
    21      True               False   True  False  False      True   
    22      True               False   True  False  False      True   
    23      True               False   True  False  False      True   
    24     False                True   True  False  False      True   
    25     False               False   True  False  False      True   
    26      True               False   True  False  False      True   
    27      True               False   True  False  False      True   
    28      True               False   True  False  False      True   
    29      True               False   True  False  False      True   
    30      True               False   True  False  False      True   
    31     False                True   True  False  False      True   
    32     False               False   True  False  False      True   
    33      True               False   True  False  False      True   
    34      True               False   True  False  False     False   
    35      True               False   True  False  False      True   
    36      True               False   True  False  False      True   
    37     False                True   True  False  False     False   
    38     False                True  False  False  False     False   
    
        ESPECIALIZACIÓN  MAESTRÍA  DOCTORADO  TOTAL G  AUXILIAR   ASISTENTE  \
    0              True     False      False    False       True      False   
    1              True     False      False    False       True      False   
    2              True     False       True    False       True      False   
    3              True     False      False    False       True      False   
    4              True     False      False    False      False      False   
    5              True     False      False    False      False      False   
    6              True     False      False    False      False      False   
    7             False     False      False    False       True      False   
    8             False     False      False    False      False      False   
    9             False     False       True    False      False       True   
    10             True     False      False    False      False      False   
    11            False     False      False    False       True      False   
    12            False     False      False    False      False      False   
    13             True     False       True    False      False      False   
    14             True     False       True    False      False      False   
    15            False     False      False    False      False      False   
    16             True     False       True    False       True      False   
    17            False     False      False    False      False      False   
    18             True     False       True    False      False       True   
    19             True     False       True    False       True      False   
    20             True     False      False    False      False      False   
    21             True     False      False    False      False      False   
    22             True     False       True    False       True      False   
    23             True     False      False    False      False      False   
    24             True     False      False    False      False      False   
    25             True     False      False    False       True      False   
    26             True     False      False    False       True      False   
    27             True     False      False    False      False      False   
    28             True     False      False    False      False      False   
    29             True     False      False    False       True      False   
    30             True     False       True    False       True      False   
    31             True     False      False    False      False      False   
    32            False     False      False    False      False      False   
    33            False     False      False    False      False      False   
    34            False     False      False    False      False      False   
    35            False      True       True    False       True      False   
    36            False     False      False    False      False      False   
    37            False     False      False    False      False      False   
    38            False     False      False    False      False      False   
    
        ASOCIADO   TITULAR  TOTAL GENERAL   
    0       False    False           False  
    1       False     True           False  
    2        True     True           False  
    3       False    False           False  
    4        True    False           False  
    5       False    False           False  
    6       False    False           False  
    7       False    False           False  
    8       False    False           False  
    9       False     True           False  
    10      False    False           False  
    11      False     True           False  
    12      False    False           False  
    13       True     True           False  
    14       True     True           False  
    15      False    False           False  
    16       True     True           False  
    17      False    False           False  
    18       True     True           False  
    19      False     True           False  
    20      False     True           False  
    21      False    False           False  
    22       True     True           False  
    23      False    False           False  
    24      False    False           False  
    25      False    False           False  
    26      False     True           False  
    27      False    False           False  
    28      False    False           False  
    29      False    False           False  
    30      False    False           False  
    31      False    False           False  
    32      False    False           False  
    33      False    False           False  
    34      False     True           False  
    35       True     True           False  
    36      False    False           False  
    37      False    False           False  
    38      False    False           False  
    

Limpia las filas donde exista al menos NAN


```python
docentes_sin_nan1 = docentes.dropna(axis=0, how='any')
print(docentes_sin_nan1)
```

    Empty DataFrame
    Columns: [Facultad, Programa Académico, TC, MT, TOTAL, PREGRADO, ESPECIALIZACIÓN, MAESTRÍA, DOCTORADO, TOTAL G, AUXILIAR , ASISTENTE, ASOCIADO , TITULAR, TOTAL GENERAL ]
    Index: []
    

Limpia las filas donde todos sus valores sean NAN


```python
docentes_sin_nan2 = docentes.dropna(axis=0, how='all')
print(docentes_sin_nan2)
```

                                           Facultad  \
    0                     CIENCIAS AGROINDUSTRIALES   
    1                                           NaN   
    2                                           NaN   
    3               Total CIENCIAS AGROINDUSTRIALES   
    4               CIENCIAS BASICAS Y TECNOLOGICAS   
    5                                           NaN   
    6                                           NaN   
    7                                           NaN   
    8         Total CIENCIAS BASICAS Y TECNOLOGICAS   
    9                          CIENCIAS DE LA SALUD   
    10                                          NaN   
    11                                          NaN   
    12                   Total CIENCIAS DE LA SALUD   
    13        CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    14                                          NaN   
    15                                          NaN   
    16                                          NaN   
    17  Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    18              CIENCIAS HUMANAS Y BELLAS ARTES   
    19                                          NaN   
    20                                          NaN   
    21                                          NaN   
    22                                          NaN   
    23                                          NaN   
    24        Total CIENCIAS HUMANAS Y BELLAS ARTES   
    25                                    EDUCACION   
    26                                          NaN   
    27                                          NaN   
    28                                          NaN   
    29                                          NaN   
    30                                          NaN   
    31                              Total EDUCACION   
    32                                   INGENIERIA   
    33                                          NaN   
    34                                          NaN   
    35                                          NaN   
    36                                          NaN   
    37                             Total INGENIERIA   
    38                                Total general   
    
                                       Programa Académico    TC   MT  TOTAL  \
    0       INGENIERIA DE ALIMENTOS                         NaN    8      8   
    1       TECNOLOGIA AGROINDUSTRIAL                       NaN    2      2   
    2       TECNOLOGIA AGROPECUARIA                         NaN    1      1   
    3                                                 NaN   NaN   11     11   
    4                                BIOLOGIA               NaN    9      9   
    5                                FISICA                 NaN   10     10   
    6                                QUIMICA                NaN   13     13   
    7          TECNOLOGIA EN INSTRUMENTACION ELECTRONICA    NaN   11     11   
    8                                                 NaN   NaN   43     43   
    9                                ENFERMERIA             2.0    4      6   
    10                               MEDICINA              27.0   16     43   
    11                   SEGURIDAD Y SALUD EN EL TRABAJO    NaN    3      3   
    12                                                NaN  29.0   23     52   
    13      ADMINISTRACION DE NEGOCIOS  PRESENCIAL          NaN    3      3   
    14                          ADMINISTRACION FINANCIERA   NaN    3      3   
    15                               CONTADURIA             NaN   20     20   
    16                                           ECONOMIA   NaN    4      4   
    17                                                NaN   NaN   30     30   
    18                               ARTES VISUAL           NaN    1      1   
    19         CIENCIAS DE LA INFORMACION Y LA DOC          NaN    2      2   
    20         COMUNICACION SOCIAL Y PERIODISMO             NaN    7      7   
    21                               FILOSOFIA              NaN    6      6   
    22                               GERONTOLOGIA           NaN    3      3   
    23                            TRABAJO SOCIAL            NaN    9      9   
    24                                                NaN   NaN   28     28   
    25  LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...   NaN   10     10   
    26  LICENCIATURA EN EDUCACION FISICA Y DEPORTES   ...   NaN    4      4   
    27  LICENCIATURA EN ESPAÑOL Y LITERATURA          ...   NaN    8      8   
    28                   LICENCIATURA EN LENGUAS MODERNAS   NaN   12     12   
    29                   LICENCIATURA EN MATEMATICAS        NaN   18     18   
    30                 LICENCIATURA EN PEDAGOGIA INFANTIL   NaN    7      7   
    31                                                NaN   NaN   59     59   
    32                                   INGENIERIA CIVIL   NaN   17     17   
    33                         INGENIERIA DE SISTEMAS       NaN   15     15   
    34      INGENIERIA ELECTRONICA                          NaN   14     14   
    35         TECNOLOGIA EN OBRAS CIVILES                  NaN    1      1   
    36         TECNOLOGIA EN TOPOGRAFIA                     NaN    8      8   
    37                                                NaN   NaN   55     55   
    38                                                NaN  29.0  249    278   
    
        PREGRADO  ESPECIALIZACIÓN  MAESTRÍA  DOCTORADO  TOTAL G  AUXILIAR   \
    0        NaN              NaN       4.0        4.0        8        NaN   
    1        NaN              NaN       1.0        1.0        2        NaN   
    2        NaN              NaN       1.0        NaN        1        NaN   
    3        NaN              NaN       6.0        5.0       11        NaN   
    4        NaN              NaN       3.0        6.0        9        2.0   
    5        NaN              NaN       2.0        8.0       10        1.0   
    6        NaN              NaN      10.0        3.0       13        3.0   
    7        NaN              1.0       8.0        2.0       11        NaN   
    8        NaN              1.0      23.0       19.0       43        6.0   
    9        NaN              1.0       5.0        NaN        6        5.0   
    10       1.0              NaN      34.0        8.0       43       18.0   
    11       NaN              1.0       1.0        1.0        3        NaN   
    12       1.0              2.0      40.0        9.0       52       23.0   
    13       NaN              NaN       3.0        NaN        3        1.0   
    14       NaN              NaN       3.0        NaN        3        1.0   
    15       NaN              2.0      17.0        1.0       20        2.0   
    16       NaN              NaN       4.0        NaN        4        NaN   
    17       NaN              2.0      27.0        1.0       30        4.0   
    18       NaN              NaN       1.0        NaN        1        1.0   
    19       NaN              NaN       2.0        NaN        2        NaN   
    20       NaN              NaN       4.0        3.0        7        1.0   
    21       NaN              NaN       3.0        3.0        6        1.0   
    22       NaN              NaN       3.0        NaN        3        NaN   
    23       NaN              NaN       6.0        3.0        9        3.0   
    24       NaN              NaN      19.0        9.0       28        6.0   
    25       NaN              NaN       5.0        5.0       10        NaN   
    26       NaN              NaN       3.0        1.0        4        NaN   
    27       NaN              NaN       6.0        2.0        8        1.0   
    28       NaN              NaN       9.0        3.0       12        7.0   
    29       NaN              NaN      11.0        7.0       18        NaN   
    30       NaN              NaN       7.0        NaN        7        NaN   
    31       NaN              NaN      41.0       18.0       59        8.0   
    32       NaN              1.0      15.0        1.0       17        9.0   
    33       NaN              1.0       9.0        5.0       15        2.0   
    34       1.0              1.0       7.0        5.0       14        3.0   
    35       NaN              1.0       NaN        NaN        1        NaN   
    36       NaN              2.0       5.0        1.0        8        1.0   
    37       1.0              6.0      36.0       12.0       55       15.0   
    38       2.0             11.0     192.0       73.0      278       62.0   
    
        ASISTENTE  ASOCIADO   TITULAR  TOTAL GENERAL   
    0         4.0        3.0      1.0               8  
    1         1.0        1.0      NaN               2  
    2         1.0        NaN      NaN               1  
    3         6.0        4.0      1.0              11  
    4         5.0        NaN      2.0               9  
    5         3.0        3.0      3.0              10  
    6         3.0        4.0      3.0              13  
    7         4.0        3.0      4.0              11  
    8        15.0       10.0     12.0              43  
    9         NaN        1.0      NaN               6  
    10       13.0        6.0      6.0              43  
    11        2.0        1.0      NaN               3  
    12       15.0        8.0      6.0              52  
    13        2.0        NaN      NaN               3  
    14        2.0        NaN      NaN               3  
    15        6.0        7.0      5.0              20  
    16        4.0        NaN      NaN               4  
    17       14.0        7.0      5.0              30  
    18        NaN        NaN      NaN               1  
    19        1.0        1.0      NaN               2  
    20        3.0        3.0      NaN               7  
    21        1.0        2.0      2.0               6  
    22        3.0        NaN      NaN               3  
    23        3.0        2.0      1.0               9  
    24       11.0        8.0      3.0              28  
    25        7.0        1.0      2.0              10  
    26        1.0        3.0      NaN               4  
    27        5.0        1.0      1.0               8  
    28        2.0        2.0      1.0              12  
    29        6.0        7.0      5.0              18  
    30        3.0        3.0      1.0               7  
    31       24.0       17.0     10.0              59  
    32        5.0        1.0      2.0              17  
    33        7.0        5.0      1.0              15  
    34        9.0        2.0      NaN              14  
    35        1.0        NaN      NaN               1  
    36        3.0        2.0      2.0               8  
    37       25.0       10.0      5.0              55  
    38      110.0       64.0     42.0             278  
    

Limpia las columnas donde exista al menos un NAN


```python
docentes_sin_nan3 = docentes.dropna(axis=1, how='any')
print(docentes_sin_nan3)
```

         MT  TOTAL  TOTAL G  TOTAL GENERAL 
    0     8      8        8               8
    1     2      2        2               2
    2     1      1        1               1
    3    11     11       11              11
    4     9      9        9               9
    5    10     10       10              10
    6    13     13       13              13
    7    11     11       11              11
    8    43     43       43              43
    9     4      6        6               6
    10   16     43       43              43
    11    3      3        3               3
    12   23     52       52              52
    13    3      3        3               3
    14    3      3        3               3
    15   20     20       20              20
    16    4      4        4               4
    17   30     30       30              30
    18    1      1        1               1
    19    2      2        2               2
    20    7      7        7               7
    21    6      6        6               6
    22    3      3        3               3
    23    9      9        9               9
    24   28     28       28              28
    25   10     10       10              10
    26    4      4        4               4
    27    8      8        8               8
    28   12     12       12              12
    29   18     18       18              18
    30    7      7        7               7
    31   59     59       59              59
    32   17     17       17              17
    33   15     15       15              15
    34   14     14       14              14
    35    1      1        1               1
    36    8      8        8               8
    37   55     55       55              55
    38  249    278      278             278
    

Llena todos los NAN con '3'


```python
docentes_nuevo = docentes.fillna(value=3)
print(docentes_nuevo)
```

                                           Facultad  \
    0                     CIENCIAS AGROINDUSTRIALES   
    1                                             3   
    2                                             3   
    3               Total CIENCIAS AGROINDUSTRIALES   
    4               CIENCIAS BASICAS Y TECNOLOGICAS   
    5                                             3   
    6                                             3   
    7                                             3   
    8         Total CIENCIAS BASICAS Y TECNOLOGICAS   
    9                          CIENCIAS DE LA SALUD   
    10                                            3   
    11                                            3   
    12                   Total CIENCIAS DE LA SALUD   
    13        CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    14                                            3   
    15                                            3   
    16                                            3   
    17  Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    18              CIENCIAS HUMANAS Y BELLAS ARTES   
    19                                            3   
    20                                            3   
    21                                            3   
    22                                            3   
    23                                            3   
    24        Total CIENCIAS HUMANAS Y BELLAS ARTES   
    25                                    EDUCACION   
    26                                            3   
    27                                            3   
    28                                            3   
    29                                            3   
    30                                            3   
    31                              Total EDUCACION   
    32                                   INGENIERIA   
    33                                            3   
    34                                            3   
    35                                            3   
    36                                            3   
    37                             Total INGENIERIA   
    38                                Total general   
    
                                       Programa Académico    TC   MT  TOTAL  \
    0       INGENIERIA DE ALIMENTOS                         3.0    8      8   
    1       TECNOLOGIA AGROINDUSTRIAL                       3.0    2      2   
    2       TECNOLOGIA AGROPECUARIA                         3.0    1      1   
    3                                                   3   3.0   11     11   
    4                                BIOLOGIA               3.0    9      9   
    5                                FISICA                 3.0   10     10   
    6                                QUIMICA                3.0   13     13   
    7          TECNOLOGIA EN INSTRUMENTACION ELECTRONICA    3.0   11     11   
    8                                                   3   3.0   43     43   
    9                                ENFERMERIA             2.0    4      6   
    10                               MEDICINA              27.0   16     43   
    11                   SEGURIDAD Y SALUD EN EL TRABAJO    3.0    3      3   
    12                                                  3  29.0   23     52   
    13      ADMINISTRACION DE NEGOCIOS  PRESENCIAL          3.0    3      3   
    14                          ADMINISTRACION FINANCIERA   3.0    3      3   
    15                               CONTADURIA             3.0   20     20   
    16                                           ECONOMIA   3.0    4      4   
    17                                                  3   3.0   30     30   
    18                               ARTES VISUAL           3.0    1      1   
    19         CIENCIAS DE LA INFORMACION Y LA DOC          3.0    2      2   
    20         COMUNICACION SOCIAL Y PERIODISMO             3.0    7      7   
    21                               FILOSOFIA              3.0    6      6   
    22                               GERONTOLOGIA           3.0    3      3   
    23                            TRABAJO SOCIAL            3.0    9      9   
    24                                                  3   3.0   28     28   
    25  LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...   3.0   10     10   
    26  LICENCIATURA EN EDUCACION FISICA Y DEPORTES   ...   3.0    4      4   
    27  LICENCIATURA EN ESPAÑOL Y LITERATURA          ...   3.0    8      8   
    28                   LICENCIATURA EN LENGUAS MODERNAS   3.0   12     12   
    29                   LICENCIATURA EN MATEMATICAS        3.0   18     18   
    30                 LICENCIATURA EN PEDAGOGIA INFANTIL   3.0    7      7   
    31                                                  3   3.0   59     59   
    32                                   INGENIERIA CIVIL   3.0   17     17   
    33                         INGENIERIA DE SISTEMAS       3.0   15     15   
    34      INGENIERIA ELECTRONICA                          3.0   14     14   
    35         TECNOLOGIA EN OBRAS CIVILES                  3.0    1      1   
    36         TECNOLOGIA EN TOPOGRAFIA                     3.0    8      8   
    37                                                  3   3.0   55     55   
    38                                                  3  29.0  249    278   
    
        PREGRADO  ESPECIALIZACIÓN  MAESTRÍA  DOCTORADO  TOTAL G  AUXILIAR   \
    0        3.0              3.0       4.0        4.0        8        3.0   
    1        3.0              3.0       1.0        1.0        2        3.0   
    2        3.0              3.0       1.0        3.0        1        3.0   
    3        3.0              3.0       6.0        5.0       11        3.0   
    4        3.0              3.0       3.0        6.0        9        2.0   
    5        3.0              3.0       2.0        8.0       10        1.0   
    6        3.0              3.0      10.0        3.0       13        3.0   
    7        3.0              1.0       8.0        2.0       11        3.0   
    8        3.0              1.0      23.0       19.0       43        6.0   
    9        3.0              1.0       5.0        3.0        6        5.0   
    10       1.0              3.0      34.0        8.0       43       18.0   
    11       3.0              1.0       1.0        1.0        3        3.0   
    12       1.0              2.0      40.0        9.0       52       23.0   
    13       3.0              3.0       3.0        3.0        3        1.0   
    14       3.0              3.0       3.0        3.0        3        1.0   
    15       3.0              2.0      17.0        1.0       20        2.0   
    16       3.0              3.0       4.0        3.0        4        3.0   
    17       3.0              2.0      27.0        1.0       30        4.0   
    18       3.0              3.0       1.0        3.0        1        1.0   
    19       3.0              3.0       2.0        3.0        2        3.0   
    20       3.0              3.0       4.0        3.0        7        1.0   
    21       3.0              3.0       3.0        3.0        6        1.0   
    22       3.0              3.0       3.0        3.0        3        3.0   
    23       3.0              3.0       6.0        3.0        9        3.0   
    24       3.0              3.0      19.0        9.0       28        6.0   
    25       3.0              3.0       5.0        5.0       10        3.0   
    26       3.0              3.0       3.0        1.0        4        3.0   
    27       3.0              3.0       6.0        2.0        8        1.0   
    28       3.0              3.0       9.0        3.0       12        7.0   
    29       3.0              3.0      11.0        7.0       18        3.0   
    30       3.0              3.0       7.0        3.0        7        3.0   
    31       3.0              3.0      41.0       18.0       59        8.0   
    32       3.0              1.0      15.0        1.0       17        9.0   
    33       3.0              1.0       9.0        5.0       15        2.0   
    34       1.0              1.0       7.0        5.0       14        3.0   
    35       3.0              1.0       3.0        3.0        1        3.0   
    36       3.0              2.0       5.0        1.0        8        1.0   
    37       1.0              6.0      36.0       12.0       55       15.0   
    38       2.0             11.0     192.0       73.0      278       62.0   
    
        ASISTENTE  ASOCIADO   TITULAR  TOTAL GENERAL   
    0         4.0        3.0      1.0               8  
    1         1.0        1.0      3.0               2  
    2         1.0        3.0      3.0               1  
    3         6.0        4.0      1.0              11  
    4         5.0        3.0      2.0               9  
    5         3.0        3.0      3.0              10  
    6         3.0        4.0      3.0              13  
    7         4.0        3.0      4.0              11  
    8        15.0       10.0     12.0              43  
    9         3.0        1.0      3.0               6  
    10       13.0        6.0      6.0              43  
    11        2.0        1.0      3.0               3  
    12       15.0        8.0      6.0              52  
    13        2.0        3.0      3.0               3  
    14        2.0        3.0      3.0               3  
    15        6.0        7.0      5.0              20  
    16        4.0        3.0      3.0               4  
    17       14.0        7.0      5.0              30  
    18        3.0        3.0      3.0               1  
    19        1.0        1.0      3.0               2  
    20        3.0        3.0      3.0               7  
    21        1.0        2.0      2.0               6  
    22        3.0        3.0      3.0               3  
    23        3.0        2.0      1.0               9  
    24       11.0        8.0      3.0              28  
    25        7.0        1.0      2.0              10  
    26        1.0        3.0      3.0               4  
    27        5.0        1.0      1.0               8  
    28        2.0        2.0      1.0              12  
    29        6.0        7.0      5.0              18  
    30        3.0        3.0      1.0               7  
    31       24.0       17.0     10.0              59  
    32        5.0        1.0      2.0              17  
    33        7.0        5.0      1.0              15  
    34        9.0        2.0      3.0              14  
    35        1.0        3.0      3.0               1  
    36        3.0        2.0      2.0               8  
    37       25.0       10.0      5.0              55  
    38      110.0       64.0     42.0             278  
    

Donde exista un NAN lo cambiará por el valor medio de dicha columna


```python
docentes_nuevo = docentes.fillna(docentes.mean())
print(docentes_nuevo)
```

                                           Facultad  \
    0                     CIENCIAS AGROINDUSTRIALES   
    1                                           NaN   
    2                                           NaN   
    3               Total CIENCIAS AGROINDUSTRIALES   
    4               CIENCIAS BASICAS Y TECNOLOGICAS   
    5                                           NaN   
    6                                           NaN   
    7                                           NaN   
    8         Total CIENCIAS BASICAS Y TECNOLOGICAS   
    9                          CIENCIAS DE LA SALUD   
    10                                          NaN   
    11                                          NaN   
    12                   Total CIENCIAS DE LA SALUD   
    13        CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    14                                          NaN   
    15                                          NaN   
    16                                          NaN   
    17  Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    18              CIENCIAS HUMANAS Y BELLAS ARTES   
    19                                          NaN   
    20                                          NaN   
    21                                          NaN   
    22                                          NaN   
    23                                          NaN   
    24        Total CIENCIAS HUMANAS Y BELLAS ARTES   
    25                                    EDUCACION   
    26                                          NaN   
    27                                          NaN   
    28                                          NaN   
    29                                          NaN   
    30                                          NaN   
    31                              Total EDUCACION   
    32                                   INGENIERIA   
    33                                          NaN   
    34                                          NaN   
    35                                          NaN   
    36                                          NaN   
    37                             Total INGENIERIA   
    38                                Total general   
    
                                       Programa Académico     TC   MT  TOTAL  \
    0       INGENIERIA DE ALIMENTOS                        21.75    8      8   
    1       TECNOLOGIA AGROINDUSTRIAL                      21.75    2      2   
    2       TECNOLOGIA AGROPECUARIA                        21.75    1      1   
    3                                                 NaN  21.75   11     11   
    4                                BIOLOGIA              21.75    9      9   
    5                                FISICA                21.75   10     10   
    6                                QUIMICA               21.75   13     13   
    7          TECNOLOGIA EN INSTRUMENTACION ELECTRONICA   21.75   11     11   
    8                                                 NaN  21.75   43     43   
    9                                ENFERMERIA             2.00    4      6   
    10                               MEDICINA              27.00   16     43   
    11                   SEGURIDAD Y SALUD EN EL TRABAJO   21.75    3      3   
    12                                                NaN  29.00   23     52   
    13      ADMINISTRACION DE NEGOCIOS  PRESENCIAL         21.75    3      3   
    14                          ADMINISTRACION FINANCIERA  21.75    3      3   
    15                               CONTADURIA            21.75   20     20   
    16                                           ECONOMIA  21.75    4      4   
    17                                                NaN  21.75   30     30   
    18                               ARTES VISUAL          21.75    1      1   
    19         CIENCIAS DE LA INFORMACION Y LA DOC         21.75    2      2   
    20         COMUNICACION SOCIAL Y PERIODISMO            21.75    7      7   
    21                               FILOSOFIA             21.75    6      6   
    22                               GERONTOLOGIA          21.75    3      3   
    23                            TRABAJO SOCIAL           21.75    9      9   
    24                                                NaN  21.75   28     28   
    25  LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...  21.75   10     10   
    26  LICENCIATURA EN EDUCACION FISICA Y DEPORTES   ...  21.75    4      4   
    27  LICENCIATURA EN ESPAÑOL Y LITERATURA          ...  21.75    8      8   
    28                   LICENCIATURA EN LENGUAS MODERNAS  21.75   12     12   
    29                   LICENCIATURA EN MATEMATICAS       21.75   18     18   
    30                 LICENCIATURA EN PEDAGOGIA INFANTIL  21.75    7      7   
    31                                                NaN  21.75   59     59   
    32                                   INGENIERIA CIVIL  21.75   17     17   
    33                         INGENIERIA DE SISTEMAS      21.75   15     15   
    34      INGENIERIA ELECTRONICA                         21.75   14     14   
    35         TECNOLOGIA EN OBRAS CIVILES                 21.75    1      1   
    36         TECNOLOGIA EN TOPOGRAFIA                    21.75    8      8   
    37                                                NaN  21.75   55     55   
    38                                                NaN  29.00  249    278   
    
        PREGRADO  ESPECIALIZACIÓN    MAESTRÍA  DOCTORADO  TOTAL G  AUXILIAR   \
    0        1.2         2.357143    4.000000   4.000000        8       7.44   
    1        1.2         2.357143    1.000000   1.000000        2       7.44   
    2        1.2         2.357143    1.000000   7.551724        1       7.44   
    3        1.2         2.357143    6.000000   5.000000       11       7.44   
    4        1.2         2.357143    3.000000   6.000000        9       2.00   
    5        1.2         2.357143    2.000000   8.000000       10       1.00   
    6        1.2         2.357143   10.000000   3.000000       13       3.00   
    7        1.2         1.000000    8.000000   2.000000       11       7.44   
    8        1.2         1.000000   23.000000  19.000000       43       6.00   
    9        1.2         1.000000    5.000000   7.551724        6       5.00   
    10       1.0         2.357143   34.000000   8.000000       43      18.00   
    11       1.2         1.000000    1.000000   1.000000        3       7.44   
    12       1.0         2.000000   40.000000   9.000000       52      23.00   
    13       1.2         2.357143    3.000000   7.551724        3       1.00   
    14       1.2         2.357143    3.000000   7.551724        3       1.00   
    15       1.2         2.000000   17.000000   1.000000       20       2.00   
    16       1.2         2.357143    4.000000   7.551724        4       7.44   
    17       1.2         2.000000   27.000000   1.000000       30       4.00   
    18       1.2         2.357143    1.000000   7.551724        1       1.00   
    19       1.2         2.357143    2.000000   7.551724        2       7.44   
    20       1.2         2.357143    4.000000   3.000000        7       1.00   
    21       1.2         2.357143    3.000000   3.000000        6       1.00   
    22       1.2         2.357143    3.000000   7.551724        3       7.44   
    23       1.2         2.357143    6.000000   3.000000        9       3.00   
    24       1.2         2.357143   19.000000   9.000000       28       6.00   
    25       1.2         2.357143    5.000000   5.000000       10       7.44   
    26       1.2         2.357143    3.000000   1.000000        4       7.44   
    27       1.2         2.357143    6.000000   2.000000        8       1.00   
    28       1.2         2.357143    9.000000   3.000000       12       7.00   
    29       1.2         2.357143   11.000000   7.000000       18       7.44   
    30       1.2         2.357143    7.000000   7.551724        7       7.44   
    31       1.2         2.357143   41.000000  18.000000       59       8.00   
    32       1.2         1.000000   15.000000   1.000000       17       9.00   
    33       1.2         1.000000    9.000000   5.000000       15       2.00   
    34       1.0         1.000000    7.000000   5.000000       14       3.00   
    35       1.2         1.000000   15.157895   7.551724        1       7.44   
    36       1.2         2.000000    5.000000   1.000000        8       1.00   
    37       1.0         6.000000   36.000000  12.000000       55      15.00   
    38       2.0        11.000000  192.000000  73.000000      278      62.00   
    
         ASISTENTE  ASOCIADO   TITULAR  TOTAL GENERAL   
    0     4.000000   3.000000     1.00               8  
    1     1.000000   1.000000     5.04               2  
    2     1.000000   6.193548     5.04               1  
    3     6.000000   4.000000     1.00              11  
    4     5.000000   6.193548     2.00               9  
    5     3.000000   3.000000     3.00              10  
    6     3.000000   4.000000     3.00              13  
    7     4.000000   3.000000     4.00              11  
    8    15.000000  10.000000    12.00              43  
    9     8.918919   1.000000     5.04               6  
    10   13.000000   6.000000     6.00              43  
    11    2.000000   1.000000     5.04               3  
    12   15.000000   8.000000     6.00              52  
    13    2.000000   6.193548     5.04               3  
    14    2.000000   6.193548     5.04               3  
    15    6.000000   7.000000     5.00              20  
    16    4.000000   6.193548     5.04               4  
    17   14.000000   7.000000     5.00              30  
    18    8.918919   6.193548     5.04               1  
    19    1.000000   1.000000     5.04               2  
    20    3.000000   3.000000     5.04               7  
    21    1.000000   2.000000     2.00               6  
    22    3.000000   6.193548     5.04               3  
    23    3.000000   2.000000     1.00               9  
    24   11.000000   8.000000     3.00              28  
    25    7.000000   1.000000     2.00              10  
    26    1.000000   3.000000     5.04               4  
    27    5.000000   1.000000     1.00               8  
    28    2.000000   2.000000     1.00              12  
    29    6.000000   7.000000     5.00              18  
    30    3.000000   3.000000     1.00               7  
    31   24.000000  17.000000    10.00              59  
    32    5.000000   1.000000     2.00              17  
    33    7.000000   5.000000     1.00              15  
    34    9.000000   2.000000     5.04              14  
    35    1.000000   6.193548     5.04               1  
    36    3.000000   2.000000     2.00               8  
    37   25.000000  10.000000     5.00              55  
    38  110.000000  64.000000    42.00             278  
    

Completa los NAN utilizando el valor de la fila i+1, en la misma columna


```python
docentes_nuevo = docentes.fillna(method='bfill', limit=1)
print(docentes_nuevo)
```

                                           Facultad  \
    0                     CIENCIAS AGROINDUSTRIALES   
    1                                           NaN   
    2               Total CIENCIAS AGROINDUSTRIALES   
    3               Total CIENCIAS AGROINDUSTRIALES   
    4               CIENCIAS BASICAS Y TECNOLOGICAS   
    5                                           NaN   
    6                                           NaN   
    7         Total CIENCIAS BASICAS Y TECNOLOGICAS   
    8         Total CIENCIAS BASICAS Y TECNOLOGICAS   
    9                          CIENCIAS DE LA SALUD   
    10                                          NaN   
    11                   Total CIENCIAS DE LA SALUD   
    12                   Total CIENCIAS DE LA SALUD   
    13        CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    14                                          NaN   
    15                                          NaN   
    16  Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    17  Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS   
    18              CIENCIAS HUMANAS Y BELLAS ARTES   
    19                                          NaN   
    20                                          NaN   
    21                                          NaN   
    22                                          NaN   
    23        Total CIENCIAS HUMANAS Y BELLAS ARTES   
    24        Total CIENCIAS HUMANAS Y BELLAS ARTES   
    25                                    EDUCACION   
    26                                          NaN   
    27                                          NaN   
    28                                          NaN   
    29                                          NaN   
    30                              Total EDUCACION   
    31                              Total EDUCACION   
    32                                   INGENIERIA   
    33                                          NaN   
    34                                          NaN   
    35                                          NaN   
    36                             Total INGENIERIA   
    37                             Total INGENIERIA   
    38                                Total general   
    
                                       Programa Académico    TC   MT  TOTAL  \
    0       INGENIERIA DE ALIMENTOS                         NaN    8      8   
    1       TECNOLOGIA AGROINDUSTRIAL                       NaN    2      2   
    2       TECNOLOGIA AGROPECUARIA                         NaN    1      1   
    3                                BIOLOGIA               NaN   11     11   
    4                                BIOLOGIA               NaN    9      9   
    5                                FISICA                 NaN   10     10   
    6                                QUIMICA                NaN   13     13   
    7          TECNOLOGIA EN INSTRUMENTACION ELECTRONICA    NaN   11     11   
    8                                ENFERMERIA             2.0   43     43   
    9                                ENFERMERIA             2.0    4      6   
    10                               MEDICINA              27.0   16     43   
    11                   SEGURIDAD Y SALUD EN EL TRABAJO   29.0    3      3   
    12      ADMINISTRACION DE NEGOCIOS  PRESENCIAL         29.0   23     52   
    13      ADMINISTRACION DE NEGOCIOS  PRESENCIAL          NaN    3      3   
    14                          ADMINISTRACION FINANCIERA   NaN    3      3   
    15                               CONTADURIA             NaN   20     20   
    16                                           ECONOMIA   NaN    4      4   
    17                               ARTES VISUAL           NaN   30     30   
    18                               ARTES VISUAL           NaN    1      1   
    19         CIENCIAS DE LA INFORMACION Y LA DOC          NaN    2      2   
    20         COMUNICACION SOCIAL Y PERIODISMO             NaN    7      7   
    21                               FILOSOFIA              NaN    6      6   
    22                               GERONTOLOGIA           NaN    3      3   
    23                            TRABAJO SOCIAL            NaN    9      9   
    24  LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...   NaN   28     28   
    25  LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...   NaN   10     10   
    26  LICENCIATURA EN EDUCACION FISICA Y DEPORTES   ...   NaN    4      4   
    27  LICENCIATURA EN ESPAÑOL Y LITERATURA          ...   NaN    8      8   
    28                   LICENCIATURA EN LENGUAS MODERNAS   NaN   12     12   
    29                   LICENCIATURA EN MATEMATICAS        NaN   18     18   
    30                 LICENCIATURA EN PEDAGOGIA INFANTIL   NaN    7      7   
    31                                   INGENIERIA CIVIL   NaN   59     59   
    32                                   INGENIERIA CIVIL   NaN   17     17   
    33                         INGENIERIA DE SISTEMAS       NaN   15     15   
    34      INGENIERIA ELECTRONICA                          NaN   14     14   
    35         TECNOLOGIA EN OBRAS CIVILES                  NaN    1      1   
    36         TECNOLOGIA EN TOPOGRAFIA                     NaN    8      8   
    37                                                NaN  29.0   55     55   
    38                                                NaN  29.0  249    278   
    
        PREGRADO  ESPECIALIZACIÓN  MAESTRÍA  DOCTORADO  TOTAL G  AUXILIAR   \
    0        NaN              NaN       4.0        4.0        8        NaN   
    1        NaN              NaN       1.0        1.0        2        NaN   
    2        NaN              NaN       1.0        5.0        1        NaN   
    3        NaN              NaN       6.0        5.0       11        2.0   
    4        NaN              NaN       3.0        6.0        9        2.0   
    5        NaN              NaN       2.0        8.0       10        1.0   
    6        NaN              1.0      10.0        3.0       13        3.0   
    7        NaN              1.0       8.0        2.0       11        6.0   
    8        NaN              1.0      23.0       19.0       43        6.0   
    9        1.0              1.0       5.0        8.0        6        5.0   
    10       1.0              1.0      34.0        8.0       43       18.0   
    11       1.0              1.0       1.0        1.0        3       23.0   
    12       1.0              2.0      40.0        9.0       52       23.0   
    13       NaN              NaN       3.0        NaN        3        1.0   
    14       NaN              2.0       3.0        1.0        3        1.0   
    15       NaN              2.0      17.0        1.0       20        2.0   
    16       NaN              2.0       4.0        1.0        4        4.0   
    17       NaN              2.0      27.0        1.0       30        4.0   
    18       NaN              NaN       1.0        NaN        1        1.0   
    19       NaN              NaN       2.0        3.0        2        1.0   
    20       NaN              NaN       4.0        3.0        7        1.0   
    21       NaN              NaN       3.0        3.0        6        1.0   
    22       NaN              NaN       3.0        3.0        3        3.0   
    23       NaN              NaN       6.0        3.0        9        3.0   
    24       NaN              NaN      19.0        9.0       28        6.0   
    25       NaN              NaN       5.0        5.0       10        NaN   
    26       NaN              NaN       3.0        1.0        4        1.0   
    27       NaN              NaN       6.0        2.0        8        1.0   
    28       NaN              NaN       9.0        3.0       12        7.0   
    29       NaN              NaN      11.0        7.0       18        NaN   
    30       NaN              NaN       7.0       18.0        7        8.0   
    31       NaN              1.0      41.0       18.0       59        8.0   
    32       NaN              1.0      15.0        1.0       17        9.0   
    33       1.0              1.0       9.0        5.0       15        2.0   
    34       1.0              1.0       7.0        5.0       14        3.0   
    35       NaN              1.0       5.0        1.0        1        1.0   
    36       1.0              2.0       5.0        1.0        8        1.0   
    37       1.0              6.0      36.0       12.0       55       15.0   
    38       2.0             11.0     192.0       73.0      278       62.0   
    
        ASISTENTE  ASOCIADO   TITULAR  TOTAL GENERAL   
    0         4.0        3.0      1.0               8  
    1         1.0        1.0      NaN               2  
    2         1.0        4.0      1.0               1  
    3         6.0        4.0      1.0              11  
    4         5.0        3.0      2.0               9  
    5         3.0        3.0      3.0              10  
    6         3.0        4.0      3.0              13  
    7         4.0        3.0      4.0              11  
    8        15.0       10.0     12.0              43  
    9        13.0        1.0      6.0               6  
    10       13.0        6.0      6.0              43  
    11        2.0        1.0      6.0               3  
    12       15.0        8.0      6.0              52  
    13        2.0        NaN      NaN               3  
    14        2.0        7.0      5.0               3  
    15        6.0        7.0      5.0              20  
    16        4.0        7.0      5.0               4  
    17       14.0        7.0      5.0              30  
    18        1.0        1.0      NaN               1  
    19        1.0        1.0      NaN               2  
    20        3.0        3.0      2.0               7  
    21        1.0        2.0      2.0               6  
    22        3.0        2.0      1.0               3  
    23        3.0        2.0      1.0               9  
    24       11.0        8.0      3.0              28  
    25        7.0        1.0      2.0              10  
    26        1.0        3.0      1.0               4  
    27        5.0        1.0      1.0               8  
    28        2.0        2.0      1.0              12  
    29        6.0        7.0      5.0              18  
    30        3.0        3.0      1.0               7  
    31       24.0       17.0     10.0              59  
    32        5.0        1.0      2.0              17  
    33        7.0        5.0      1.0              15  
    34        9.0        2.0      NaN              14  
    35        1.0        2.0      2.0               1  
    36        3.0        2.0      2.0               8  
    37       25.0       10.0      5.0              55  
    38      110.0       64.0     42.0             278  
    

Retorna una serie con el resultado de evaluar la condición de que la celda de la columna 'DOCTORADO' sea ">=5"


```python
docentes['DOCTORADO'] >= 5
```




    0     False
    1     False
    2     False
    3      True
    4      True
    5      True
    6     False
    7     False
    8      True
    9     False
    10     True
    11    False
    12     True
    13    False
    14    False
    15    False
    16    False
    17    False
    18    False
    19    False
    20    False
    21    False
    22    False
    23    False
    24     True
    25     True
    26    False
    27    False
    28    False
    29     True
    30    False
    31     True
    32    False
    33     True
    34     True
    35    False
    36    False
    37     True
    38     True
    Name: DOCTORADO, dtype: bool



Retorna un DataFrame con unicamente las filas donde su columna 'DOCTORADO'  satisfaga que el valor sea ">=5"


```python
docentes[docentes['DOCTORADO'] >=5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Total CIENCIAS AGROINDUSTRIALES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11</td>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>11</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>BIOLOGIA</td>
      <td>NaN</td>
      <td>9</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>9</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>FISICA</td>
      <td>NaN</td>
      <td>10</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>10</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Total CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43</td>
      <td>43</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>19.0</td>
      <td>43</td>
      <td>6.0</td>
      <td>15.0</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>43</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>MEDICINA</td>
      <td>27.0</td>
      <td>16</td>
      <td>43</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>43</td>
      <td>18.0</td>
      <td>13.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>43</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Total CIENCIAS DE LA SALUD</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>23</td>
      <td>52</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>40.0</td>
      <td>9.0</td>
      <td>52</td>
      <td>23.0</td>
      <td>15.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>52</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Total CIENCIAS HUMANAS Y BELLAS ARTES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28</td>
      <td>28</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19.0</td>
      <td>9.0</td>
      <td>28</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>25</th>
      <td>EDUCACION</td>
      <td>LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...</td>
      <td>NaN</td>
      <td>10</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>10</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NaN</td>
      <td>LICENCIATURA EN MATEMATICAS</td>
      <td>NaN</td>
      <td>18</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>7.0</td>
      <td>18</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>18</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Total EDUCACION</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59</td>
      <td>59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.0</td>
      <td>18.0</td>
      <td>59</td>
      <td>8.0</td>
      <td>24.0</td>
      <td>17.0</td>
      <td>10.0</td>
      <td>59</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NaN</td>
      <td>INGENIERIA DE SISTEMAS</td>
      <td>NaN</td>
      <td>15</td>
      <td>15</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>15</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>34</th>
      <td>NaN</td>
      <td>INGENIERIA ELECTRONICA</td>
      <td>NaN</td>
      <td>14</td>
      <td>14</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>14</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>14</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Total INGENIERIA</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55</td>
      <td>55</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>36.0</td>
      <td>12.0</td>
      <td>55</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>55</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Total general</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>249</td>
      <td>278</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>192.0</td>
      <td>73.0</td>
      <td>278</td>
      <td>62.0</td>
      <td>110.0</td>
      <td>64.0</td>
      <td>42.0</td>
      <td>278</td>
    </tr>
  </tbody>
</table>
</div>



Retorna La Columna "Programas Académicos" donde su valor de 'DOCTORADO' sea ">=5"


```python
docentes['Programa Académico'][docentes['DOCTORADO'] >=5]
```




    3                                                   NaN
    4                                  BIOLOGIA            
    5                                  FISICA              
    8                                                   NaN
    10                                 MEDICINA            
    12                                                  NaN
    24                                                  NaN
    25    LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...
    29                     LICENCIATURA EN MATEMATICAS     
    31                                                  NaN
    33                           INGENIERIA DE SISTEMAS    
    34        INGENIERIA ELECTRONICA                       
    37                                                  NaN
    38                                                  NaN
    Name: Programa Académico, dtype: object



Retorna un DataFrame con unicamente las filas en donde se cumplan las condiciones de que su 'DOCTORADO' sea ">=5" y a su vez la 'MAESTRÍA" sea ">=7"


```python
docentes[(docentes['DOCTORADO'] >=5) & (docentes['MAESTRÍA'] >=7)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Total CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43</td>
      <td>43</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>19.0</td>
      <td>43</td>
      <td>6.0</td>
      <td>15.0</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>43</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>MEDICINA</td>
      <td>27.0</td>
      <td>16</td>
      <td>43</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>43</td>
      <td>18.0</td>
      <td>13.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>43</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Total CIENCIAS DE LA SALUD</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>23</td>
      <td>52</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>40.0</td>
      <td>9.0</td>
      <td>52</td>
      <td>23.0</td>
      <td>15.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>52</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Total CIENCIAS HUMANAS Y BELLAS ARTES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28</td>
      <td>28</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19.0</td>
      <td>9.0</td>
      <td>28</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NaN</td>
      <td>LICENCIATURA EN MATEMATICAS</td>
      <td>NaN</td>
      <td>18</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>7.0</td>
      <td>18</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>18</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Total EDUCACION</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59</td>
      <td>59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.0</td>
      <td>18.0</td>
      <td>59</td>
      <td>8.0</td>
      <td>24.0</td>
      <td>17.0</td>
      <td>10.0</td>
      <td>59</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NaN</td>
      <td>INGENIERIA DE SISTEMAS</td>
      <td>NaN</td>
      <td>15</td>
      <td>15</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>15</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>34</th>
      <td>NaN</td>
      <td>INGENIERIA ELECTRONICA</td>
      <td>NaN</td>
      <td>14</td>
      <td>14</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>14</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>14</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Total INGENIERIA</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55</td>
      <td>55</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>36.0</td>
      <td>12.0</td>
      <td>55</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>55</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Total general</td>
      <td>NaN</td>
      <td>29.0</td>
      <td>249</td>
      <td>278</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>192.0</td>
      <td>73.0</td>
      <td>278</td>
      <td>62.0</td>
      <td>110.0</td>
      <td>64.0</td>
      <td>42.0</td>
      <td>278</td>
    </tr>
  </tbody>
</table>
</div>



Las filas en donde no se cumpla con la condición de que la 'ESPECIALIZACIÓN' sea ">=2" se llenarán de NaN


```python
docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.where(docentes_n2['ESPECIALIZACIÓN']>=2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Total CIENCIAS DE LA SALUD</td>
      <td>0</td>
      <td>29.0</td>
      <td>23.0</td>
      <td>52.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>40.0</td>
      <td>9.0</td>
      <td>52.0</td>
      <td>23.0</td>
      <td>15.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>CONTADURIA</td>
      <td>0.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Total CIENCIAS ECONOMICAS Y ADMINISTRATIVAS</td>
      <td>0</td>
      <td>0.0</td>
      <td>30.0</td>
      <td>30.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>27.0</td>
      <td>1.0</td>
      <td>30.0</td>
      <td>4.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>36</th>
      <td>0</td>
      <td>TECNOLOGIA EN TOPOGRAFIA</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Total INGENIERIA</td>
      <td>0</td>
      <td>0.0</td>
      <td>55.0</td>
      <td>55.0</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>36.0</td>
      <td>12.0</td>
      <td>55.0</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Total general</td>
      <td>0</td>
      <td>29.0</td>
      <td>249.0</td>
      <td>278.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>192.0</td>
      <td>73.0</td>
      <td>278.0</td>
      <td>62.0</td>
      <td>110.0</td>
      <td>64.0</td>
      <td>42.0</td>
      <td>278.0</td>
    </tr>
  </tbody>
</table>
</div>



Las filas en donde se cumpla con la condición de que la 'ESPECIALIZACIÓN' sea ">=2" se llenarán de NaN


```python
docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.mask(docentes_n2['ESPECIALIZACIÓN']>=2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CIENCIAS AGROINDUSTRIALES</td>
      <td>INGENIERIA DE ALIMENTOS</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>TECNOLOGIA AGROINDUSTRIAL</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>TECNOLOGIA AGROPECUARIA</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Total CIENCIAS AGROINDUSTRIALES</td>
      <td>0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>BIOLOGIA</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>FISICA</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>QUIMICA</td>
      <td>0.0</td>
      <td>13.0</td>
      <td>13.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>3.0</td>
      <td>13.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>TECNOLOGIA EN INSTRUMENTACION ELECTRONICA</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Total CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>0</td>
      <td>0.0</td>
      <td>43.0</td>
      <td>43.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>19.0</td>
      <td>43.0</td>
      <td>6.0</td>
      <td>15.0</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CIENCIAS DE LA SALUD</td>
      <td>ENFERMERIA</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>MEDICINA</td>
      <td>27.0</td>
      <td>16.0</td>
      <td>43.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>43.0</td>
      <td>18.0</td>
      <td>13.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>SEGURIDAD Y SALUD EN EL TRABAJO</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>CIENCIAS ECONOMICAS Y ADMINISTRATIVAS</td>
      <td>ADMINISTRACION DE NEGOCIOS  PRESENCIAL</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0</td>
      <td>ADMINISTRACION FINANCIERA</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0</td>
      <td>ECONOMIA</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>CIENCIAS HUMANAS Y BELLAS ARTES</td>
      <td>ARTES VISUAL</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0</td>
      <td>CIENCIAS DE LA INFORMACION Y LA DOC</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0</td>
      <td>COMUNICACION SOCIAL Y PERIODISMO</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0</td>
      <td>FILOSOFIA</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0</td>
      <td>GERONTOLOGIA</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0</td>
      <td>TRABAJO SOCIAL</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Total CIENCIAS HUMANAS Y BELLAS ARTES</td>
      <td>0</td>
      <td>0.0</td>
      <td>28.0</td>
      <td>28.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>19.0</td>
      <td>9.0</td>
      <td>28.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>EDUCACION</td>
      <td>LICENCIATURA DE BIOLOGIA Y EDUCACION AMBIENTAL...</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0</td>
      <td>LICENCIATURA EN EDUCACION FISICA Y DEPORTES   ...</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0</td>
      <td>LICENCIATURA EN ESPAÑOL Y LITERATURA          ...</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0</td>
      <td>LICENCIATURA EN LENGUAS MODERNAS</td>
      <td>0.0</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>12.0</td>
      <td>7.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0</td>
      <td>LICENCIATURA EN MATEMATICAS</td>
      <td>0.0</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>7.0</td>
      <td>18.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>0</td>
      <td>LICENCIATURA EN PEDAGOGIA INFANTIL</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Total EDUCACION</td>
      <td>0</td>
      <td>0.0</td>
      <td>59.0</td>
      <td>59.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>41.0</td>
      <td>18.0</td>
      <td>59.0</td>
      <td>8.0</td>
      <td>24.0</td>
      <td>17.0</td>
      <td>10.0</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>INGENIERIA</td>
      <td>INGENIERIA CIVIL</td>
      <td>0.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>17.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>0</td>
      <td>INGENIERIA DE SISTEMAS</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>15.0</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>0</td>
      <td>INGENIERIA ELECTRONICA</td>
      <td>0.0</td>
      <td>14.0</td>
      <td>14.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>14.0</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0</td>
      <td>TECNOLOGIA EN OBRAS CIVILES</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Retorna un DataFrame con valores True o False, evaluando si el valor de cada celda se encuentra en la lista "[5,8,10,12,14]"


```python
docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.isin([5,8,10,12,14])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>13</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>15</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>16</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>17</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>18</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>19</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>20</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>21</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>22</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>23</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>24</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>25</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>26</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>27</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>28</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>29</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>30</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>31</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>32</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>33</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>34</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>36</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>37</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>38</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



Retorna un DataFrame con las filas donde se cumpla la condición de que el valor de la columna 'DOCTORADO' sea mayor al de la celda 'MAESTRÍA'


```python
docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.query('DOCTORADO > MAESTRÍA')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facultad</th>
      <th>Programa Académico</th>
      <th>TC</th>
      <th>MT</th>
      <th>TOTAL</th>
      <th>PREGRADO</th>
      <th>ESPECIALIZACIÓN</th>
      <th>MAESTRÍA</th>
      <th>DOCTORADO</th>
      <th>TOTAL G</th>
      <th>AUXILIAR</th>
      <th>ASISTENTE</th>
      <th>ASOCIADO</th>
      <th>TITULAR</th>
      <th>TOTAL GENERAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>CIENCIAS BASICAS Y TECNOLOGICAS</td>
      <td>BIOLOGIA</td>
      <td>0.0</td>
      <td>9</td>
      <td>9</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>9</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>FISICA</td>
      <td>0.0</td>
      <td>10</td>
      <td>10</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>10</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



Devuelve una Serie con la evaluación de la operación 'DOCTORADO+MAESTRÍA'


```python
docentes_n2 = docentes.fillna(value=0)
docentes_n2
docentes_n2.eval('DOCTORADO + MAESTRÍA')
```




    0       8.0
    1       2.0
    2       1.0
    3      11.0
    4       9.0
    5      10.0
    6      13.0
    7      10.0
    8      42.0
    9       5.0
    10     42.0
    11      2.0
    12     49.0
    13      3.0
    14      3.0
    15     18.0
    16      4.0
    17     28.0
    18      1.0
    19      2.0
    20      7.0
    21      6.0
    22      3.0
    23      9.0
    24     28.0
    25     10.0
    26      4.0
    27      8.0
    28     12.0
    29     18.0
    30      7.0
    31     59.0
    32     16.0
    33     14.0
    34     12.0
    35      0.0
    36      6.0
    37     48.0
    38    265.0
    dtype: float64


