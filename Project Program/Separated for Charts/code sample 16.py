import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# 🔍 Check for missing/null values
print("🧾 Missing/Null Values Summary:\n")
missing_values = df.isnull().sum()

# Display only columns with missing values
missing_values = missing_values[missing_values > 0]
if not missing_values.empty:
    print(missing_values)
else:
    print("✅ No missing or null values found in the dataset.")

# Optional: Show percentage of missing data
print("\n📊 Percentage of Missing Data per Column:")
percent_missing = (df.isnull().mean() * 100).round(2)
print(percent_missing[percent_missing > 0])
