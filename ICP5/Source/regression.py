import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('train.csv')

train.SalePrice.describe()

# scatter plot between Garage
print(train[['GarageArea']])
plt.scatter(train.GarageArea,train.SalePrice, alpha=.75, color='r')
plt.show()

fltr = train[(train.GarageArea < 1000) & (train.GarageArea > 200)]
plt.scatter(fltr.GarageArea,fltr.SalePrice, alpha=.75, color='b')
plt.show()
