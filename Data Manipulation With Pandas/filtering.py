import pandas as pd

# Filter students with grades above 85 from students.csv
students = pd.read_csv("Python/CSV-Files/students.csv")

honors = students[students["grade"] > 85]
print(honors)

# Find all employees with salary > $50,000 in employees.csv
emps = pd.read_csv("Python/CSV-Files/employees.csv")

higherThan50k = emps[emps["salary"] > 50000]
print(higherThan50k)

# Show products with price less than $20 in products.csv
products = pd.read_csv("Python/CSV-Files/products.csv")

lessThan20 = products[products["price"] < 20]
print(lessThan20)