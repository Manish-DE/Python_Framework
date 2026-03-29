import pandas as pd
from dataset import df


print("Original DataFrame:")
print(df)

print("\nDataFrame with Missing Values:")
print(df.isnull())
print("\nDataFrame with Missing Values Count:")
print(df.isnull().sum())
