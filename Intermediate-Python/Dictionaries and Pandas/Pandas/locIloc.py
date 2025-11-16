import pandas as pd

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
    "indexes" : [0, 1, 2, 3, 4]
}

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print("Original DataFrame", end='\n')
print(brics)

print(end='\n')
print(brics.loc[["BR", "RU"], ["country", "capital"]])
print(end='\n')
print(brics.iloc[[0, 1], [0, 1]])
#The print statements above are the exact same