import pandas as pd
from dataset import df

print("Original DataFrame:")
print(df)   


# df.dropna(inplace=True)
# print("\nDataFrame after removing all rows:")
# print(df)

# df.fillna(0, inplace=True)
# print("\nDataFrame after filling missing values with 0:")
# print(df)


df['Age'].fillna({'Age': df['Age'].mean()}, inplace=True)
print("\nDataFrame after filling missing values in 'Age' with mean:")   
df['Salary'].fillna(df['Salary'].median(), inplace=True)
print(df)