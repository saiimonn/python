import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Python/Intermediate-Python/CSV-Files/closing_stock.csv", index_col = 0)
df.plot()
plt.grid()
plt.title('Closing stock value of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Value')

plt.show()