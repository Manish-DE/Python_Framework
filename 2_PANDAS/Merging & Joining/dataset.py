import pandas as pd

customers = {
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Country': ['USA', 'UK', 'USA', 'Canada']   
}
orders = {
    'OrderID': [101, 102, 103, 104, 105, 106],
    'CustomerID': [1, 2, 1, 3, 4, 5],
    'OrderDate': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06' ],
    'Amount': [250, 150, 300, 200, 400, 500]
}   

