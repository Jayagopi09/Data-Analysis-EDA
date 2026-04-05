import sqlite3
import pandas as pd

# Create a connection to an in-memory SQLite database
conn = sqlite3.connect(":memory:")
df=pd.DataFrame(conn)

# Write the dataframe to SQL
df.to_sql("uber_requests", conn, index=False, if_exists="replace")

# Run an example SQL query
query = "SELECT Status, COUNT(*) FROM uber_requests GROUP BY Status;"
result_df = pd.read_sql_query(query, conn)
print(result_df)
