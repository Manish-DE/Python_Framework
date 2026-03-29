import pandas as pd
from dataset import df

# df.sort_values(by='Age', ascending=True, inplace=True)
# print("DataFrame sorted by Age in ascending order:")    
# print(df)

df.sort_values(by=['Age', 'Salary'], ascending=[True, False], inplace=True)
print("DataFrame sorted by Age in ascending order:")

print(df)
