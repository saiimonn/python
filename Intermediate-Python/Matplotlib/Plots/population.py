import matplotlib.pyplot as plt

years = [1950, 1970, 1990, 2010, 2030]
pop = [2.932, 3.948, 5.221, 7.141, 8.490]

plt.plot(years, pop)
plt.xlabel('Years')
plt.ylabel('Population')
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()