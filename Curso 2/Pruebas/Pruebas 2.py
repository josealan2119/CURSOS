import pandas as pd


reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

#Se puede usar el nombre de la comlumna para solo regresar esos valores
print(reviews.country)

print(reviews['country'])

#Aqui esta indicado el numero de fila y la columna con ese nombre
print(reviews['country'][0])


#--------------------ILOC FUNCION----------------------------
#Solo trabaja con numeros

#Retorna toda la informacion de la fila del numero indicado
print(reviews.iloc[0])

#Indicas de q fila a fila y columans regresas
print(reviews.iloc[:,0])

print(reviews.iloc[:3, 0])

print(reviews.iloc[1:3,0])

print(reviews.iloc[[0, 1, 2], 0]) # Tambien se le puede pasar otra lista

print(reviews.iloc[-5:]) #He indicar las ultimas tambien


#------------------------ LOC FUNCION -----------------------

#Solo retorna el valor dl numero de fila y el nombre de la columna
print(reviews.loc[0,'country'])


#Retorna las filas indicadas y de las columnas del nombre que se requiera
print(reviews.loc[:,['taster_name', 'taster_twitter_handle', 'points']])


#Pasar una columna como orden q principal de la tabla
print(reviews.set_index('title'))


###-------------------------- CONDICIONALES -------------------------

reviews.country == 'Italy'

reviews.loc[reviews.country == 'Italy']

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

## Que solo los paises q sean tales
reviews.loc[reviews.country.isin(['Italy', 'France'])]

# Donde el precio no sea nulo
reviews.loc[reviews.price.notnull()]


####----------------------Asignar Datos--------------------

#Crea una nueva columna donde todas las filas van a tener valor de everyone
reviews['critic'] = 'everyone'

# Crea una secunecia la cual va desde 12342 hasta el 0 disminuyendo -1
reviews['index_backwards'] = range(len(reviews), 0, -1)
