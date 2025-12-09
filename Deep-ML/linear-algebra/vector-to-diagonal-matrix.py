import numpy as np

def make_diagonal(x):
	retArr = []
	for i in range(len(x)):
		retArr.append([])
		for j in range(len(x)):
			if i == j:
				retArr[i].append(x[i])
			else:
				retArr[i].append(0)
	return retArr
	pass

x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)