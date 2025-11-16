import pandas as pd

df = pd.read_csv("Python/CSV-Files/e-commerce_transactions.csv")

print(df.head())

print(df.drop_duplicates(subset = "item_category"))

print(df["item_category"].value_counts()) #counts how many entries there are of each category