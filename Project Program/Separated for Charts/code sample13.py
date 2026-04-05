import pandas as pd

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# Count rows and columns
num_rows, num_columns = df.shape

# Print the results
print(f"Total Rows: {num_rows}")
print(f"Total Columns: {num_columns}")
