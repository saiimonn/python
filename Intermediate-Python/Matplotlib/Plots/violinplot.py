import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(loc=mean, scale=std, size=100)
        for mean, std in zip([0, 1, 2, 3], [0.5, 1, 0.8, 1.2])]

plt.violinplot(data, showmeans=True, showmedians=True)

plt.xticks([1, 2, 3, 4], ['Group A', 'Group B', 'Group C', 'Group D'])
plt.title("Violin Plot")
plt.ylabel("Value")
plt.grid(True)
plt.show()