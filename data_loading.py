import pandas as pd

# Loading the dataset
df = pd.read_csv('rides_data.csv')

# Displaying the first 5 rows of the DataFrame to understand its structure and content.
print("--- Initial Data Snapshot (First 5 Rows) ---")
print(df.head())

# Summary of the DataFrame's info, including data types and non-null counts.
print("\n" + "-"*50 + "\n")
print("--- DataFrame Information ---")
df.info()

# Statistical summary for numerical columns to identify potential outliers.
print("\n" + "-"*50 + "\n")
print("--- Statistical Summary of Numerical Columns ---")
print(df.describe())
