import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

# Load the dataset
file_path = "Uber Request Data.csv"
df = pd.read_csv(file_path)

# Show missing value summary
print("🧾 Missing Values Summary:")
missing_counts = df.isnull().sum()
print(missing_counts[missing_counts > 0])

# Optional: Percentage of missing data
print("\n📊 Missing Data Percentage:")
missing_percent = (df.isnull().mean() * 100).round(2)
print(missing_percent[missing_percent > 0])

# 🔍 Visualization using seaborn heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Heatmap of Missing Values")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()

# 📊 Visualization using missingno matrix
msno.matrix(df)
plt.title("Missing Value Matrix")
plt.show()

# 📉 Missing value bar chart
msno.bar(df)
plt.title("Missing Value Count per Column")
plt.show()
