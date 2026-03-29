import pandas as pd
from dataset import customers, orders

df_region1 = pd.DataFrame({
    'Region': ['North', 'South', 'East'],
    'Sales': [100, 200, 150]
})
df_region2 = pd.DataFrame({
    'Region': ['West', 'Central'],  
    'Sales': [250, 300]
})   
# Create DataFrames



print("Concatenated DataFrame (Rows):")
print(pd.concat([df_region1, df_region2], axis=0, ignore_index=True))
print("\nConcatenated DataFrame (Columns):")
print(pd.concat([df_region1, df_region2], axis=1, ignore_index=True))  
# Concatenate DataFrames with different columns
# customers_df2 = customers_df.copy()
# customers_df2['NewColumn'] = ['A', 'B', 'C', 'D']   
# print("\nConcatenated DataFrame with Different Columns:")
# print(pd.concat([customers_df, customers_df2], axis=0, ignore_index=True, sort=False))
# # Concatenate DataFrames with different indices
# customers_df3 = customers_df.copy()
# customers_df3.index = [10, 11, 12, 13]
# print("\nConcatenated DataFrame with Different Indices:")   
# print(pd.concat([customers_df, customers_df3], axis=0, ignore_index=True, sort=False))