import csv
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Ingresar al sitio y descargar el CSV con los datos
url="https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true"
response = requests.get(url)
with open(os.path.join("Archivo", "Data.csv"), "wb") as f:
    f.write(response.content)

#Abrir el CSV que se descargó y obtener la información
data =pd.read_csv('Archivo/Data.csv')
data.head()

data.columns=['ID', 'Fecha de notificación', 'Código DIVIPOLA', 'Ciudad', 'Departamento', 'Atencion', 'Edad', 'Sexo', 'Tipo', 'Estado', 'País de procedencia', 'FIS', 'Fecha de muerte', 'Fecha diagnostico', 'Fecha recuperado', 'fecha reporte web', 'Tipo recuperación', 'Codigo departamento', 'Codigo pais', 'Pertenencia etnica', 'Nombre grupo etnico']

d={'m':'M', 'f':'F','F':'F', 'M':'M'}
data['Sexo']=data['Sexo'].apply(lambda x:d[x])


#GRÁFICAS DE BARRAS
fig1=plt.figure(figsize=(12,6))
data.Departamento.value_counts().plot(kind='bar', alpha=0.5)
plt.title('Número de Casos Totales según Departamento en Colombia')
plt.show()

fig=plt.figure(figsize=(12,6))
data.Sexo.value_counts().plot(kind='bar', alpha=0.5)
plt.title('Número de Casos según el Sexo')
plt.show()

fig2=plt.figure(figsize=(12,6))
data.Atencion[data.Atencion == "Recuperado"].value_counts().plot(kind='bar', alpha=0.5)
plt.title('Número de Casos de Recuperados en Colombia')
plt.show()

fig3=plt.figure(figsize=(12,6))
data.Atencion[data.Atencion == "Fallecido"].value_counts().plot(kind='bar', alpha=0.5)
plt.title('Número de Casos de Fallecidos en Colombia')
plt.show()

#GRÁFICAS DE TORTAS

fig1=plt.figure(figsize=(12,6))
plt.pie(data.Sexo.value_counts(), autopct="%1.1f%%", shadow=True, radius= .9)
plt.title('Porcentaje de Casos según el Sexo', bbox={"facecolor":"0.8","pad":5})
plt.legend( labels= data.Sexo.value_counts().index.unique(), loc='upper right')
plt.show()

fig1=plt.figure(figsize=(12,6))
plt.pie(data.Atencion.value_counts(), autopct="%1.1f%%", shadow=True, radius= .999)
plt.title('Porcentaje de la situación de los contagiados en Colombia', bbox={"facecolor":"0.8","pad":5})
plt.legend( labels=['%s, %1.1f%%' % (
        l, (float(s) / data.ID.iloc[-1]) * 100) for l, s in zip(data.Atencion.value_counts().index.unique(), data.Atencion.value_counts())], loc='upper right')
plt.show()
