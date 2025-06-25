import pandas as pd

# How to convert a series of date-strings to a timeseries
date_series = pd.Series(['2025-01-01', '2025-02-01', '2025-03-01'])
datetime_series = pd.to_datetime(date_series)
print(datetime_series)
print(type(datetime_series[1]))

'''Create two DataFrames, df1 and df2, with a common column (e.g., 'ID').
- Perform an inner merge on this common column and display the resulting DataFrame.
- Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values 
  are handled in the resulting DataFrame. Right Join and Index-Based Join.
- Perform a right join using pd.merge() on a common column, then perform a join using 
  df.join() based on the index. Compare the results. Merging with Multiple Keys.'''

# Create two Dataframes
df1 = pd.DataFrame({
    'ID':[101,102,103,104,105],
    'Name': ['A1','A2','A3','A4','A5'],
    'Subject': ['sub1','sub2','sub3','sub4','sub5']
}, index=[1,2,3,4,5]
)
print(df1)
print()
df2 = pd.DataFrame({
    'ID':[103,104,105,106,107],
    'Name': ['B1','B2','B3','B4','B5'],
    'Subject': ['sub1','subB','sub3','subD','sub5']
}, index=[1,2,3,4,5])
print(df2)
print()

# Inner merge on common column id
# In inner join all the rows which have a same id in df1 and df2 are printed
result = df1.merge(df2, how='inner', on='ID')
print("Inner Merge: ")
print(result)
print()

# Left join of df1 and df2 on the ID column
# In left join all the tuples of df1 are in the output and NaN is in place of the missing values of df2
left_join = df1.merge(df2, how='left', on='ID')
print("Left Join: ")
print(left_join)
print()

# Right Join
right_join = df1.merge(df2, how='right', on='ID')
print("Right Join: ")
print(right_join)
print()

# Index Based join using join() method
# Join is based on the index(not column), missing values produce NaN
df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')
print(df1_index)
print(df2_index)
print()
index_join = df1_index.join(df2_index, how='left', lsuffix = '_df1', rsuffix = '_df2')
print("Index Join: ")
print(index_join)
print()

# New df1 and df2
df1 = pd.DataFrame({
    'ID': [101, 102, 103],
    'Dept': ['HR', 'IT', 'Finance'],
    'Name': ['Amit', 'Priya', 'Ravi']
})

df2 = pd.DataFrame({
    'ID': [102, 103, 104],
    'Dept': ['IT', 'Finance', 'HR'],
    'Score': [88, 92, 76]
})

# Right join using pd.merge()
right_join = pd.merge(df1, df2, how='right', on='ID')
print("Right Join using pd.merge(): ")
print(right_join)
print()

# Right join using join() method and index-based
right_join = df1.set_index('ID').join(df2.set_index('ID'), how='right', lsuffix = '_df1', rsuffix = '_df2')
print("Right Join using index-based join: ")
print(right_join)
print()

# Right Join using pd.merge():
# - Joins based on one or more column values (e.g., 'ID')
# - Automatically handles overlapping column names with _x and _y
# - Supports multi-key joins (e.g., on=['ID', 'Dept'])

# Right Join using df.join():
# - Joins based on index (row labels), not columns
# - Both DataFrames must have the same index or be reset accordingly
# - Overlapping columns must be manually handled with lsuffix/rsuffix
# - Does not support joining on multiple columns directly


# Merge with multiple common keys
multi_key = pd.merge(df1, df2, on=['ID', 'Dept'], how='inner')
print("Merge on Multiple Keys ['ID', 'Dept']: ")
print(multi_key)
print()


''' Create three DataFrames. Vertically concatenate two of them using pd.concat(), then merge 
the resulting DataFrame with the third DataFrame on a common key.'''

df1 = pd.DataFrame({
    'EmpID': [101, 102],
    'Name': ['Amit', 'Priya'],
    'Dept': ['HR', 'IT']
})

df2 = pd.DataFrame({
    'EmpID': [103, 104],
    'Name': ['Ravi', 'Neha'],
    'Dept': ['Finance', 'Marketing']
})

df3 = pd.DataFrame({
    'EmpID': [102, 103, 104],
    'Salary': [60000, 55000, 58000]
})

# Vertically concatenate df1 and df2
concat_df = pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame(concatenation of df1 and df2): ")
print(concat_df)
print()

# Merge with df3 on EmpID
merged_df = pd.merge(concat_df, df3, on='EmpID', how='inner')
print("Final Merged DataFrame: ")
print(merged_df)
print()

'''Explain the primary differences between df.join() and pd.merge()'''

# pd.merge():
# - Joins on columns (like SQL joins)
# - Supports multiple join keys (on=['col1', 'col2'])
# - Can join on index with left_index=True / right_index=True

# df.join():
# - Joins on index by default
# - Can join on a column using 'on' parameter
# - Simpler syntax but limited to 1 key

