# Develop a program that reads a .csv dataset file using Pandas library and display
# the following content of the dataset.
# a) First five rows of the dataset
# b) Complete data of the dataset
# c) Summary or metadata of the dataset.

import pandas as pd

df = pd.read_csv("Students.csv")

print("a> first five rows of da dataset:")
print(df.head()) #head by default shows 5 rows


print("\n-------------------------------------\n")

print("b> display da complete dataset:")
print(df)

print("\n-------------------------------------\n")


print("c> summary or metadata of da dataset:")
print(df.info())   # gives info about columns, data types, non-null values

# Optional if you want statistcal summary (numerical columns)
print("\n-------------------------------------\n")

print("additional: Statistical summary of numeric columns:")
print(df.describe())


