#PARA QUE FUNCIONE TIENES QUE ELEGIR EL ENTORNO VIRTUAL Y INSTALAR LO QUE NECESITES

import pandas as pd

#Comprobacion si realmente Pandas fue importado Correctamente
print("Hello panda is working ...")


#Crear un DataFrame (Arreglo de Datos)
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)

df = pd.DataFrame({'Bob':['I liked','I dont Like'], 'Emili':['Pretty good', 'Bland']})
print(df)


#INDEX nos sirve para darle un SIGNIFICADO a la PRIMERA COLUMNA
df = pd.DataFrame({'Bob':['I like it', 'Its auful'], 
                   'Sam':['Pretty good', 'Bland']},
                   index=['Producto 1', 'Producto 2']) 
print(df)


#SERIES nos sirve para crear una Serie (COLUMNA)
df = pd.Series([1,2,3,4,5])

print(df)

#NAME nos da nombre al Areglo de que trata
df = pd.Series([30,45,50], index=['2015 sales','2020 sales','2025 sales'],
               name='Product A')

print(df)


#Leer Archivos csv o cualquier otro que se pueda
df = pd.read_csv("data.csv")
print(df)

#Shape indica el numero de filas y columnas (3,6)
print(df.shape)

#Head solo nos da las 5 primeras filas
print(df.head)


wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.head())
