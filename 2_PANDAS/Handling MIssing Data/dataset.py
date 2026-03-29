import pandas as pd

data ={
    "Name": ['Rahul', None, 'Ravi','Aditi', 'Manish', 'Manas', 'Sita', 'Gita', 'Riya'],
    "Age": [25, 30, 35, 28, 32, None, 26, 31, 27],
    "City": ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', None, 'Jaipur'],
    "Salary": [50000, 60000, 55000, 70000, 65000, 72000, 58000, 62000, 64000], 
    "Performance Score": [80, 90, 85, 95, 88, 92, 75, 78, 82],
    "Joining Date": pd.to_datetime(['2020-01-15', '2019-03-22', '2021-07-30', '2018-11-05', '2022-02-10', '2017-06-18', '2023-04-25', '2016-09-12', '2024-08-01'])
    }
df = pd.DataFrame(data)

