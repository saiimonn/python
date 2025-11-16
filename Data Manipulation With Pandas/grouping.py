# Calculate average sales by product category from sales.csv
import pandas as pd

df = pd.read_csv("Python/CSV-Files/sales.csv")

proCat = df.groupby("product")["price"].mean()
print(proCat)

# Find total transaction amount by customer from e-commerce_transactions.csv
transaction = pd.read_csv("Python/CSV-Files/e-commerce_transactions.csv")

transAmt = transaction.groupby("user_id")["purchase_amount"].sum()
print(transAmt)

# Group employees by department and calculate average salary
emps = pd.read_csv("Python/CSV-Files/employees.csv")

empDept = emps.groupby("department")["salary"].mean()
print(empDept)