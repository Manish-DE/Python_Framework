import pandas as pd
from dataset import df

high_salary = df[df['Salary'] > 60000]
print("Rows with Salary greater than 100000:")
print(high_salary) 