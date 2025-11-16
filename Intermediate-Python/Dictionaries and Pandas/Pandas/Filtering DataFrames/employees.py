import pandas as pd
import numpy as np

employees = [
    {"name": "Anna", "age": 28, "salary": 72000},
    {"name": "Ben", "age": 35, "salary": 68000},
    {"name": "Cory", "age": 40, "salary": 75000},
]

emps = pd.DataFrame(employees)
#You have a list of dictionaries representing employees. 
# Print the names of employees who are older than 30 and have a salary greater than 70,000.
print(emps[np.logical_and(emps["age"] > 30, emps["salary"] > 70000)])