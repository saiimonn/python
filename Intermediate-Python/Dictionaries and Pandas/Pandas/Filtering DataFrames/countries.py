import pandas as pd
import numpy as np

data = {
    "country": ["Canada", "Germany", "Japan", "Australia", "Mexico"],
    "capital": ["Ottawa", "Berlin", "Tokyo", "Canberra", "Mexico City"],
    "area": [9.985, 0.357, 0.378, 7.692, 1.964],  # in million sq km
    "population": [38.25, 83.02, 125.7, 25.69, 126.0],  # in millions
    "index": [0, 1, 2, 3, 4]
}

countries = pd.DataFrame(data)
countries.index = ["CAN", "GER", "JAP", "AUS", "MEX"]

print("Original DataFrame:", end='\n\n')

print(countries[countries["area"] < 5])