import pandas as pd

data = {
    "Time": [1, 2, 3, 4, 5],
    "Value": [10, None, 30, None, 50],
}

df= pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nDataFrame with Missing Values:")

# list of interpolate methods: 
#linear, polynomial, time, spline, and nearest methods
df['Value'] = df['Value'].interpolate(method='linear')  
print(df)
