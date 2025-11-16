def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(a[0])
    cols = len(a)
    b = []

    for i in range(rows):
        b.append([])
        for j in range(cols):
            b[i].append(a[j][i])
    return b

print(transpose_matrix(a = [[1, 2, 3], [4, 5, 6]]))