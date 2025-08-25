import pandas as pd
from sklearn.tree import DecisionTreeRegressor


melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

#print(melbourne_data.columns)

print(melbourne_data.shape)

#BORRA TODA 
melbourne_data = melbourne_data.dropna(axis=0)

print(melbourne_data.shape)


y = melbourne_data.Price

print(y)

print(y.shape)

#FEATURES Array de lemenos que determinar el caluclo del TARGET(En este caso el precio)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]

print(X.describe)



## ESTO YA ES PARA CREAR EL MODELO

#CREA EL MODELO
melbourne_model = DecisionTreeRegressor(random_state=1)

#ENTRENA EL MODELO CON X y y
melbourne_model.fit(X, y)


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

print(y.head)