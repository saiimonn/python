import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = (np.array(matrix) * scalar).tolist()

    return result

print(scalar_multiply(matrix = [[1, 2], [3, 4]], scalar = 2))