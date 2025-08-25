import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

#EJERCICIO 1

reviews.groupby('taster_twitter_handle').size()

#EJERCICO 2

reviews.groupby('price')['points'].max().sort_index()


#EJERCICIO 3

price_extremes = reviews.groupby('variety')['price'].agg([min, max])
