import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89])
np_weight = np.array([65.4, 59.2, 63.6, 88.5])

meas = np.array([np_height, np_weight])

for i in meas: #prints the 2d array in brackets
    print(i)

for i in np.nditer(meas): #prints the 2d array by line
    print(i)