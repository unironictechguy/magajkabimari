import pandas as pd

df = pd.read_csv('odi_runs.csv')

print("Original Dataset:")
print(df)

print("\n-------------------------------------\n")

# -----------------------------
# Step 2: Split dataset randomly using sample()
# -----------------------------
# Randomly select 50% of rows for first split
split1 = df.sample(frac=0.5, random_state=42)

# Remaining rows for second split
split2 = df.drop(split1.index)

print("Split 1 (Random Sample):")
print(split1)

print("\n-------------------------------------\n")

print("Split 2 (Remaining Data):")
print(split2)

print("\n-------------------------------------\n")

# -----------------------------
# Step 3: Merge the two splits back together
# -----------------------------
merged_df = pd.concat([split1, split2]).sort_index().reset_index(drop=True)

print("Merged Dataset (After Joining Split 1 and Split 2):")
print(merged_df)