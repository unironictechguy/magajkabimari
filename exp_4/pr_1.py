import pandas as pd

df = pd.read_csv('odi_runs.csv')

# print(df.head())

print("\n-------------------------------------\n")

#slicing rows and columns
print("Slicing first three rows, columns Player and Runs")
print(df.loc[0:2, ["Player", "Runs"]])

print("\n-------------------------------------\n")
print("Dicing: Player w Avg > 50")
print(df[df['Average']> 50])

print("\n-------------------------------------\n")

#  Multiple condition dicing: Average>50 AND StrikeRate>90
print("Players with Average>50 AND StrikeRate>90")
print(df.loc[(df["Average"]>50) & (df["StrikeRate"]>90), ["Player","Average","StrikeRate"]])


print("\n-------------------------------------\n")

# iloc examples 

print("iloc: first 3 rows and last 3 columns")
print(df.iloc[0:3, -3:])

print("\n-------------------------------------\n")
print("iloc: rows 2-5, columns 0-2 (Player, Matches, Runs)")
print(df.iloc[2:6,0:3])