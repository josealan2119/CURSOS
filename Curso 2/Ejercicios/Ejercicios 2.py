import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

#EJERCICIO 1

desc = reviews.description
print(desc)


#EJERCICIO 2
desc = reviews.description[0]
print(desc)


#EJERCICIO 3
first_row = reviews.iloc[0]
print(first_row)


#EJERCICIO 4
first_descriptions = reviews.loc[:9,'description']
print(first_descriptions)


#EJERCICIO 5
sample_reviews = reviews.iloc[[1,2,3,5,8]]
print(sample_reviews)


#EJERCICIO 6 
df = reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]
print(df)


#EJERCICIO 7
df = reviews.loc[0:99,['country','variety']]
print(df)


#EJERCICIO 8
italian_wines = reviews.loc[reviews.country == 'Italy']
print(italian_wines)


#EJERCICIO 9
top_oceania_wines =  reviews.loc[(reviews.points >= 95) & (reviews.country.isin(['Australia','New Zealand']))]
print(top_oceania_wines)