import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# Loop through each column and print unique values
print("Unique values in each column:\n")
for column in df.columns:
    unique_vals = df[column].unique()
    print(f"{column} ({len(unique_vals)} unique values):")
    print(unique_vals[:10])  # Show only first 10 unique values for brevity
    print("-" * 50)
