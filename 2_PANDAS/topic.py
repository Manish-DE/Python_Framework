import pandas as pd
from dataset import df


print("DataFrame Info:")
print(df)

print("\nDataFrame Shape:", df.shape)
print("\nDataFrame Columns:", df.columns)
# print("\nDataFrame Index:", df.index)
# print("\nDataFrame Data Types:", df.dtypes)
# print("\nDataFrame Memory Usage:", df.memory_usage(deep=True))

df.columns = df.columns[::-1]  # Reverse the order of columns
print("\nUpdated DataFrame Columns:", df.columns)
