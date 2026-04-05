import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# Display basic information
print("📋 Dataset Info:")
print(df.info())  # Includes column names, non-null counts, and data types

print("\n📊 Column-wise Summary Statistics:")
print(df.describe(include='all'))  # Summary for numeric and categorical columns

print("\n🧾 Column Names:")
print(df.columns.tolist())  # List all column names

print("\n🔍 Missing Values in Each Column:")
print(df.isnull().sum())  # Count of missing values per column
