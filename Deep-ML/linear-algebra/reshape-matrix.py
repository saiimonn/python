import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    if new_shape[0] == len(a) and new_shape[1] == len(a[0]):
        return a

    if new_shape[0] != len(a[0]) and new_shape[1] != len(a):
        return []
    
    reshaped_matrix = np.reshape(a, new_shape)

    return reshaped_matrix.tolist()

print(reshape_matrix(a = [[1, 2, 3, 4], [5, 6, 7, 8]], new_shape= (4, 2)))