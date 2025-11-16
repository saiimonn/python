import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = np.array(matrix)

    if mode == "column":
        return means.mean(axis=0).tolist()
    elif mode == "row":
        return means.mean(axis=1).tolist()
    
print(calculate_matrix_mean(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'))