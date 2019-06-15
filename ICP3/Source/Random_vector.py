import numpy as np

x = np.random.random_integers(1,20,15)
print("Input:\n")
print(x)
x[np.where(x == np.amax(x))] = 0
print(x)

