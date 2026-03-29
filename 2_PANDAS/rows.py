#head()
#tail()

import pandas as pd


df = pd.read_json("sample_Data.json")

# Display the first 5 rows of the DataFrame
print("First 5 rows:")
print(df.head(10))


print("\nLast 5 rows:")
print(df.tail(10))