import pandas as pd                 #Estructuras de datos como DataFrames
import matplotlib.pyplot as plt     #Crear gráficos
import seaborn as sns               #Libreria avanzada para visualización de datos
import numpy as np                  #Operaciones númericas

df =pd.read_csv("superstore.csv",encoding="unicode_escape")     # Leer el archivo CSV "superstore.csv" y cargarlo en un DataFrame
df.info()   # Mostrar información general del DataFrame (como número de filas, columnas, y tipo de datos)

# Crear nuevas columnas con el orden: mes, año y día
df["Order Date"]= pd.to_datetime(df["Order Date"],format='%m/%d/%Y')
df["Ship Date"]= pd.to_datetime(df["Ship Date"],format='%m/%d/%Y')
df["dt_month"] = df["Order Date"].dt.month
df["dt_year"] = df["Order Date"].dt.year
df["dt_dia"] = df["Order Date"].dt.day 


plt.figure(figsize=(12,6))      # Ajustar el tamaño de la figura
sns.barplot(x= "dt_month", y= "Sales", data=df)     #Graficar el total de ventas por mes
plt.show()          # Mostrar el gráfico


plt.figure(figsize=(12,6))      # Ajustar el tamaño de la figura
sns.kdeplot(x="ship date", data=df)     #Curva de desnsidad
plt.show()      # Mostrar el gráfico




