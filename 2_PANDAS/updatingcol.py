import pandas as pd
from dataset import df


print(df)

df.loc[df['Salary'] > 60000, 'Bonus'] = df['Salary'] * 0.1
print("DataFrame with Bonus Column Updated for High Salary:")   
print(df)

df['Salary'] = df['Salary'] * 1.05  
print("DataFrame with Bonus Column Updated for High Salary:")   
print(df)