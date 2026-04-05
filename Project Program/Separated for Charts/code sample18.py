import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Display the column names
print("Columns in the dataset:")
print(df.columns.tolist())
