import pandas as pd

# read data from Excel file into a pandas dataframe
#df = pd.read_excel("SampleSuperstore.xlsx")

#df = read_json("sample_Data.json")

# df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# print(df)

data ={
    "Name": ['Rahul', 'Rohit', 'Ravi'],
    "Age": [25, 30, 35],
    "City": ['Delhi', 'Mumbai', 'Bangalore']    
}
# Create a DataFrame from the data
df2 = pd.DataFrame(data)
print(df2)

# Save the DataFrame to a CSV file
#df2.to_csv("sample_data.csv", index=False)


# Save the DataFrame to an Excel file
#df2.to_excel("sample_data.xlsx", index=False)

# Save the DataFrame to a JSON file
df2.to_json("sample_data_trasform.json", index=False)