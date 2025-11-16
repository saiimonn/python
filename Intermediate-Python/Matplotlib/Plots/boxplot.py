import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 100)

plt.boxplot(data)
plt.title('Basic Boxplot')
plt.show()