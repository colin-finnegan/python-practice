"""

Basics of Pandas library
Author: Colin Finnegan
Date: 11/9/2026

"""


import pandas as pd

#dictionary, each key becomes a column name and each list becaomes that columns values
data = {
    'name': ['Ann', 'Ben', 'Cara', 'Dev'],
    'sales': [200, 150, 300, 120],
    'region': ['East', 'West', 'East', 'West'],
}

df = pd.DataFrame(data)
print(df)
print("\n")
print(df.head()) # first 5 rows
print("\n")
print(df.shape)  # (4, 3) 4 rows, 3 columns
print("\n")
print(df.columns) # column names
print("\n")
print(df.dtypes) # data type of each column
print("\n")
print(df['sales']) # sales column
print("\n")
print(df['name']) # name column
print("\n")
print(df['sales'].mean()) #average of sales
print("\n")
print(df[df['sales'] > 150]) # only rows where sales is greater than 150
print("\n")
df['bonus'] = df['sales'] * 0.1 #create new column
print(df[df['region'] == 'East'])
print(df[(df['region'] == 'East') & (df['sales'] > 200)]) #must use (condition 1) & (condition 2), using 'and' will raise an error
print(df.sort_values('sales', ascending=False)) #sort_values returns a new, sorted dataframe, and doesn't change df
print()

print(df.groupby('region')['sales'].mean()) # splits the rows into groups by region, picks the sales column, and takes the mean of each group
