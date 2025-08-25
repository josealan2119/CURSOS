import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)


#EJERCICIO 1

median_points = reviews.points.median()
print(median_points)

#EJERCICIO 2

countries = reviews.country.unique()
print(countries)


#EJERCICIO 3

reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)


#EJERCICIO 4

c = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - c)
print(centered_price)


#EJERCICIO 5

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_wine)

#EJERCICIO 6

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])


#EJERCICIO 7

def assign_stars(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(assign_stars, axis=1)
