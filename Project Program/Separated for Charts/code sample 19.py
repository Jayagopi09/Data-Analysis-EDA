import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# Display first few rows (optional for preview)
print("First 5 rows of the dataset:")
print(df.head())

# General info about dataset
print("\nDataset Info:")
print(df.info())

# Description of numerical columns
print("\nStatistical Summary (Numerical Columns):")
print(df.describe())

# Description of non-numerical (categorical/text) columns
print("\nSummary of Categorical Columns:")
print(df.describe(include='object'))
