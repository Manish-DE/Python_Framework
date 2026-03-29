import pandas as pd
from dataset import customers, orders

# Create DataFrames
customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)
# Merge DataFrames on CustomerID
inner_merged_df = pd.merge(customers_df, orders_df, on='CustomerID', how='inner')
# Display the merged DataFrame
print("Merged DataFrame (Inner Join):")
#print(inner_merged_df)

# Merge DataFrames with left join
left_merged_df = pd.merge(customers_df, orders_df, on='CustomerID', how='left')
# Display the left merged DataFrame 
print("\nMerged DataFrame (Left Join):")
#print(left_merged_df)

# Merge DataFrames with right join
right_merged_df = pd.merge(customers_df, orders_df, on='CustomerID', how='right')
# Display the right merged DataFrame
print("\nMerged DataFrame (Right Join):")
#print(right_merged_df)

# Merge DataFrames with outer join
outer_merged_df = pd.merge(customers_df, orders_df, on='CustomerID', how='outer')
# Display the outer merged DataFrame
print("\nMerged DataFrame (Outer Join):")
print(outer_merged_df)

# Merge DataFrames with cross join
cross_merged_df = pd.merge(customers_df, orders_df, how='cross')
# Display the cross merged DataFrame
print("\nMerged DataFrame (Cross Join):")
print(cross_merged_df)






