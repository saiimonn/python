import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
   np_matrix = np.array(matrix)
   print(np.linalg.det(np_matrix))

    # return eigenvalues

print(calculate_eigenvalues(matrix = [[2, 1], [1, 2]]))