import numpy as np

def calculate_contrast(img) -> int:
    rows = len(img)
    cols = len(img[0])
    min = img[0][0]
    max = 0

    for i in range(rows):
        if np.max(img[i]) > max:
            max = np.max(img[i])
        
        if np.min(img[i]) < min:
            min = np.min(img[i])

    return max - min

print(calculate_contrast(np.array([[0, 50], [200, 255]])))