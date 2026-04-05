import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# Find duplicate rows
duplicates = df[df.duplicated()]

# Print the number of duplicate rows
print(f"🔁 Number of duplicate rows: {duplicates.shape[0]}")

# Optional: Display the duplicate rows
if not duplicates.empty:
    print("\n📋 Duplicate Rows:")
    print(duplicates)
else:
    print("✅ No duplicate rows found.")
