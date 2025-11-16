import matplotlib.pyplot as plt

popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
languages = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
x_pos = [i for i, _ in enumerate(languages)]

plt.barh(x_pos, popularity, color = 'green')
plt.yticks(x_pos, languages)

plt.grid()


plt.show()