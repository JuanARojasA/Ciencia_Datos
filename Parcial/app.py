from flask import Flask, send_file, request, render_template

import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns

consumer_key = "twmdBkv5270o4JnPYF7jHyXGr"
consumer_secret = "t5GhlyjtaHptDFPiWMj8CshCjmJwtQyF0kfaWucix6OISFewKO"
acces_token = "1075083295497601024-ugtqbslvEeLTm7LaYwwobAw0Ina9iI"
acces_token_secret = "BKS9VH2N0c7j6Bv5AD4WsZ1A2sPtsf7jMaBzgVEV2bMbW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    return render_template('index.html')

@app.route('/analisisIndividual', methods=['GET','POST'])
def analisisIndividual():    
    if request.method == 'POST':       
        nombreEquipo = request.form.get('selecTeam')
        df = obtener_df_equipo_tweets(nombreEquipo)
        d = obtener_datos_equipo(nombreEquipo)        
        graficarDF(df, nombreEquipo)
        return render_template('resultadosIndividual.html', team=d)
    else:
        return render_template('resultadosIndividual.html')

@app.route('/analisisgeneral', methods=['GET','POST'])
def analisisGeneral():    
    if request.method == 'POST':        
        df = obtener_df_todos()
        d = obtener_datos_correlacion(df)
        graficarDFGeneral(df)
        return render_template('resultadoGeneral.html', data=d)
    else:
        return render_template('resultadoGeneral.html')
# Funciones para obtener los datos de un equipo especifico
def obtener_df_equipo_tweets(equipo):
    #obtener la informacion    
    msgs = []
    msg =[]
    for tweet in tweepy.Cursor(api.search, q=equipo).items(200):
        msg = [tweet.text, tweet.source, tweet.created_at] 
        msg = tuple(msg)                    
        msgs.append(msg)
    df= pd.DataFrame(msgs,columns=['Texto', 'Dispositivo', 'Fecha Creacion'])
    return df

def obtener_datos_equipo(equipo):
    team = api.get_user(screen_name='@'+equipo)    
    r = {
        'nombre' : team.name,
        'screenNombre' : team.screen_name,
        'seguidores' : team.followers_count,
        'tweets' : team.statuses_count,
        'locacion' : team.location,
        'fechaCreacion' : team.created_at,
        'nombreCod' : equipo
    }
    return r
# Funciones para obtener los datos de todos los equipos
def obtener_df_todos():
    equipos = ['TeamVitality', 'VeloceEsports', 'SNG_Esports', 'Mousesports', 'KnightsGG', 'GhostGaming', 'G2Esports', 'TeamReciprocity']
    tweets = []
    seguidores = []
    fechaInicio = []
    locacion = []
    for i in equipos:
        tweets.append(obtener_tweets_equipo(i))
        seguidores.append(obtener_seguidores_equipo(i))
        fechaInicio.append(obtener_fecha_equipo(i))
        locacion.append(obtener_locacion_equipo(i))
    d = {'Tweets':tweets, 'Seguidores':seguidores, 'FechaInicio':fechaInicio, 'Locacion':locacion}
    return pd.DataFrame(data=d, index=equipos)


def obtener_tweets_equipo(equipo):
    team = api.get_user(screen_name='@'+equipo)
    return team.statuses_count

def obtener_seguidores_equipo(equipo):
    team = api.get_user(screen_name='@'+equipo)
    return team.followers_count

def obtener_fecha_equipo(equipo):
    team = api.get_user(screen_name='@'+equipo)
    return team.created_at

def obtener_locacion_equipo(equipo):
    team = api.get_user(screen_name='@'+equipo)
    return team.location

def obtener_datos_correlacion(df):
    tweets = list(df['Tweets'])
    seguidores = list(df['Seguidores'])
    return np.corrcoef(tweets, seguidores)

def Porcentaje(Series):
    return (Series*100)/200
    
def graficarDF(df, dfn): 
    serieDis = df['Dispositivo'].value_counts()
    serieDis = serieDis.pipe(Porcentaje)
    dataDis= pd.DataFrame(serieDis)
    labels = list(dataDis.index)
    sizes = list(dataDis['Dispositivo'])
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('static/img/' + dfn + 'Pie.png')

    serieFecha = df.apply(lambda x: x['Fecha Creacion'].hour, axis=1)
    dataHoras = pd.DataFrame(serieFecha, columns=['Hora'])
    dataHorasConteo = pd.DataFrame(dataHoras['Hora'].value_counts())
    dataHorasConteo.plot(kind='bar',use_index=True,y="Hora",color='#D10000', title='Numero de tweets por hora',layout=('Tweets','Horas'))
    plt.savefig('static/img/' + dfn + 'Bar.png')

def graficarDFGeneral(df):
    graficar_correlacion(df)
    #Graficar los Tweets de cada Equipo
    df.plot(kind='bar',use_index=True,y="Tweets",color='#A100A0', title='Num de tweets por equipo',layout=('Cantidad','Equipo'))
    plt.savefig('static/img/tweetsConteo.png')
    #Graficar los Tweets de cada Equipo
    df.plot(kind='bar',use_index=True,y="Seguidores",color='#A1BBA0', title='Num de Seguidores por equipo',layout=('Cantidad','Equipo'))
    plt.savefig('static/img/seguidoresConteo.png')
    #Graficar los años
    serieFecha = df.apply(lambda x: x['FechaInicio'].year, axis=1)
    dataAno = pd.DataFrame(serieFecha, columns=['Ano'])
    dataAnoConteo = pd.DataFrame(dataAno['Ano'].value_counts())
    dataAnoConteo.plot(kind='bar',use_index=True,y="Ano",color='#E10000', title='Fechas de creación de equipo',layout=('Cantidad','Equipo'))
    plt.savefig('static/img/anoConteo.png')
    
def graficar_correlacion(df):
    #Graficar matriz de correlación
    sns.heatmap(df.corr(), square=True, annot=True)
    plt.savefig('static/img/correlacion.png')

if __name__ == '__main__':
    app.run(debug = True, port=8000)

