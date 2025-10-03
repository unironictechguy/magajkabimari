import pandas as pd

df = pd.read_csv('Indian_Comedians.csv')

print("Original Dataset:")
print(df)

print("\n-------------------------------------\n")

numeric_cols = ["Age", "Specials", "YouTube_Subscribers_Millions",
                "Instagram_Followers_Millions", "Popularity_Rating"]

print("a) Describe:")
print(df[numeric_cols].describe())

print("\n-------------------------------------\n")

print("b) Max:")
print(df[numeric_cols].max())

print("\n-------------------------------------\n")

print("c) Min:")
print(df[numeric_cols].min())

print("\n-------------------------------------\n")

print("d) Mean:")
print(df[numeric_cols].mean())

print("\n-------------------------------------\n")

print("e) Median:")
print(df[numeric_cols].median())

print("\n-------------------------------------\n")

print("f) Count:")
print(df.count())  # count works on all columns

print("\n-------------------------------------\n")

print("g) Standard Deviation (std):")
print(df[numeric_cols].std())

print("\n-------------------------------------\n")

print("h) Correlation (corr):")
print(df[numeric_cols].corr())