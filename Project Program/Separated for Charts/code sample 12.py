# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset
file_path = "Uber Request Data.csv"  # Ensure this CSV file is in the same directory as your script
df = pd.read_csv(file_path)

# Step 3: Display basic dataset information
print("📝 Dataset Info:")
print(df.info())  # Shows data types and missing values

print("\n📊 First 5 Rows of the Dataset:")
print(df.head())  # Shows the top 5 rows

print("\n🧮 Summary Statistics:")
print(df.describe(include='all'))  # Gives a statistical summary for all columns
