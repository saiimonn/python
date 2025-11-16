import numpy as np
print(6 > 5 and 4 < 8, end='\n')

bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])

print(np.logical_and(bmi > 21, bmi < 22), end='\n')
print(bmi[np.logical_and(bmi > 21, bmi < 22)], end='\n')