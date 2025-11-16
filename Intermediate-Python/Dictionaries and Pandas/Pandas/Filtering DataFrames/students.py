import pandas as pd
import numpy as np

students = [
    {"name": "Alice", "grade": 75, "honor": True},
    {"name": "Bob", "grade": 74, "honor": False},
    {"name": "Charlie", "grade": 80, "honor": False},
    {"name": "Diana", "grade": 75, "honor": False},
]

stud = pd.DataFrame(students)

#	•	Their grade is above 75
#	•	OR they scored exactly 75 and are on the honor list

passers = np.logical_or(stud["grade"] > 75, np.logical_and(stud["grade"] == 75, stud["honor"] == True))
print(stud[passers])