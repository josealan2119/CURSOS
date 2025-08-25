import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)


###---------------------FUNCIONES----------------

#Realiza resumenes simples los cuales cambian depende del tipo de dato
print(reviews.points.describe())

print(reviews.taster_name.describe())

#Ver la media de una columna

print(reviews.points.mean())


#Ver lo valores unico de una columna en un array

print(reviews.taster_name.unique())


#Ver los valores unicos de la columna y ver con que frecuencia aparecen

print(reviews.taster_name.value_counts())


#-----------------MAPAS--------------------
#Mapa aqui se le resta la media a cada fila y se crea un nuevo dataframe pero solo de esa columna, los demas datos se pierden

review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))


#En este caso se crean metodos q se van a realizar en cada fila y se regresa un dataframe con los datos altrerados de la fila y los otros q tiene
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
#Si fuera Index lo q se tendria q hacer una funcion que transforme cada columna


##---------------------- Opciones mas rapidas que map

#Forma mas rapida de hacer el mapeo que hace lo mismo
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

#Combinar informacion 
reviews.country + " - " + reviews.region_1

