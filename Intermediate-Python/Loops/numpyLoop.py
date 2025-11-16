import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89])
np_weight = np.array([65.4, 59.2, 63.6, 88.5])

bmi = np_weight / np_height ** 2

for i in bmi:
    print(i)