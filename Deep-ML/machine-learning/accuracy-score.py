import numpy as np

def accuracy_score(y_true, y_pred):
    correct = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            correct += 1
        
    return correct / len(y_true)

print(accuracy_score(np.array([1, 0, 1, 1, 0, 1]), np.array([1, 0, 0, 1, 0, 1])))