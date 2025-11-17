import numpy as np

def cosine_similarity(v1, v2):
    if np.size(v1) != np.size(v2):
        return
    
    if np.size(v1) == 0 or np.size(v2) == 0:
        return
    
    dot_product = np.dot(v1, v2)
    
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)

    return round((dot_product / (v1_norm * v2_norm)), 3)

print(cosine_similarity(v1 = np.array([1, 0, 7]), v2 = np.array([0, 1, 3])))