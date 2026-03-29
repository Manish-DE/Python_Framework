import pandas as pd
from dataset import df



df["Bonus"] = df["Salary"] * 0.1
print("DataFrame with Bonus Column:")
print(df)

df.insert(2, "Department", ["HR", "Finance", "IT", "Marketing", "Sales", "Operations", "R&D", "Legal", "Customer Service"])
df.insert(2, "ID", [101, 102, 103, 104, 105, 106, 107, 108, 109])
print("\nDataFrame with Department Column Added:")  
print(df)