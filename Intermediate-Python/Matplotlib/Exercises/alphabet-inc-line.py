import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Python/Intermediate-Python/CSV-Files/fdata.csv", sep = ',', parse_dates = True, index_col = 0, names = ['Open', 'High', 'Low', 'Close'])
df.plot()
plt.show()