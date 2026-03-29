import pandas as pd
from dataset import df

print(df)

df.drop(columns=['Salary', "Age"], inplace=True)
print("\nDataFrame after removing Bonus Column:")
print(df)

