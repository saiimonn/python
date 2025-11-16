import pandas as pd

df = pd.read_csv("Python/CSV-Files/student_grades.csv")

def Mean(column):
    return column.mean()

def Median(col):
    return col.median()

def pct30(col):
    return col.quantile(0.3) #returns 30th percentile of col

print(df.head())

print(df["math_score"].agg(Mean))
print(df[["math_score", "english_score", "science_score"]].agg([Mean, Median]))

print(df[["math_score", "english_score", "science_score"]].agg(pct30))