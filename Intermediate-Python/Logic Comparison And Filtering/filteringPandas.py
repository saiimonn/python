#Initializing BRICS data from dictionary and turn it to DataFrame
import pandas as pd
import numpy as np

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
    "index": [0, 1, 2, 3, 4]
}

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print("Original DataFrame", end='\n\n')
print(brics, end='\n\n')

#TASK: Select countries with area over 8 million km2
#step 1 - select area column
#step 2 - do comparision on area column
#step 3 - use result to select countries

is_greater = brics["area"] > 8

print(brics[is_greater], end='\n\n')

print(brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)], end='\n\n')
#print countries with areas that are greater than 8 and less than 10 mill