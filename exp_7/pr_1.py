# 🧹 Practical – Data Cleaning using Pandas
# Tasks:
# a) Identify null values
# b) Identify empty values
# c) Identify incorrect timestamps

import pandas as pd

# Step 1️⃣: Read the CSV file
df = pd.read_csv("Employee_Attendance.csv")

# Step 2️⃣: Display the dataset
# print("Original Dataset:\n", df, "\n")

# Step 3️⃣: Identify NULL (NaN) values
print("🔹 Checking for NULL values (NaN):\n")
print(df.isnull())              # Shows True where value is NaN
print("\nCount of NULL values per column:\n")
print(df.isnull().sum())        # Total NaNs per column

# Step 4️⃣: Identify EMPTY ("") values
print("\n🔹 Checking for EMPTY values (blank cells):\n")
print(df.eq(""))                # True for empty strings
print("\nCount of EMPTY values per column:\n")
print(df.eq("").sum())

# Step 5️⃣: Identify INCORRECT TIMESTAMPS
print("\n🔹 Checking for INCORRECT timestamps:\n")

# Define which columns are supposed to have dates/times
time_cols = ["Check_In_Time", "Check_Out_Time"]

for col in time_cols:
    print(f"\nChecking column: {col}")
    try:
        # Try to convert each column into datetime
        pd.to_datetime(df[col], format="%Y-%m-%d %H:%M:%S", errors="raise")
        print("✅ All timestamps are valid!")
    except Exception as e:
        print("❌ Invalid timestamps found in column:", col)
        # 'coerce' replaces invalid values with NaT (Not a Time)
        valid_time = pd.to_datetime(df[col], errors="coerce")
        print("Rows with incorrect timestamps:\n", df[valid_time.isna()])
