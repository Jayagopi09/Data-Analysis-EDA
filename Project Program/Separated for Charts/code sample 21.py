import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("Uber Request Data.csv")

# Step 2: Rename columns for consistency (remove spaces and lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 3: Convert timestamps to datetime format
df['request_timestamp'] = pd.to_datetime(df['request_timestamp'], dayfirst=True, errors='coerce')
df['drop_timestamp'] = pd.to_datetime(df['drop_timestamp'], dayfirst=True, errors='coerce')

# Step 4: Check and handle missing values
missing_summary = df.isnull().sum()
print("Missing values per column:\n", missing_summary)

# Step 5: Drop duplicate rows if any
df.drop_duplicates(inplace=True)

# Step 6: Create additional time-based features
df['request_hour'] = df['request_timestamp'].dt.hour
df['request_day'] = df['request_timestamp'].dt.date

# Step 7: Optional – filter out rows with invalid timestamps if needed
df = df[df['request_timestamp'].notnull()]

# Final check
print("\nCleaned dataset preview:")
print(df.head())
