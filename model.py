import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('C:/Users/rahil/Rahil/KJ Somaiya/Sem-III/ML-DS Projects/Fuel Cosumption Deployed Using Flask/FuelConsumptionCo2.csv')
df = df.dropna()
df = df.drop(['MODELYEAR', 'MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE', 'FUELCONSUMPTION_COMB'], axis = 1)

x = df.iloc[:, 0:5].values
y = df.iloc[:, -1].values
train_x, test_x, train_y, test_y = tts(x, y, test_size = 0.2, random_state = 0)

linreg = LR()
linreg.fit(train_x, train_y)
pred_y = linreg.predict(test_x)
accuracy = linreg.score(test_x, test_y)
print(accuracy * 100, "%")
print(np.abs(test_y - pred_y).mean())
