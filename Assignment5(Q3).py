import pandas as pd

# Data Iteration
# Different ways to iterate over rows in Python DataFrame
data = [
    ('Anaya', 30),
    ('Shreya', 25),
    ('Maya', 32)
]
df = pd.DataFrame(data, columns=['name', 'age'], index=[1,2,3])
print("Pandas DataFrame:")
print(df)
print()

print(df.loc[2])        #Returns row 2
print()
print(df.loc[[1,3]])    #Returns row 1 and 3
print()
for i in range(len(df)):
    print(f"Name: {df.iloc[i]['name']}, Age: {df.iloc[i]['age']}")

df.index = ['Person1','Person2','Person3']
print(df)
print()

print(df.loc['Person3'])
print()

# Selecting rows in Dataframe based on conditions
df = pd.DataFrame({
    'name': ['Anaya', 'Shreya', 'Maya', 'Kavya', 'Diya'],
    'age': [30, 25, 32, 34, 28],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai']
})
print(df)
print()

print(df[df['age'] > 30])       #Select rows where age > 30
print()
print(df[(df['age'] > 30) & (df['city'] == 'Delhi')])   #Age > 30 AND city is "Delhi"
print()
print(df[(df['age'] < 30) | (df['city'] == 'Mumbai')])  #Age < 30 OR city is "Mumbai"
print()
print(df[~(df['city'] == 'Delhi')])     #Using ~ for NOT Condition
print()
print(df.columns)
print()

# Select any row from DataFrame using iloc[]
row = df.iloc[2]
print(row)
print()

print(df.iloc[[2,4]])
print()

print(df.iloc[1,0])     #[1,0]-> 1 is index label 1 of column and 0 indicates the 0th row
print()

print(df.iloc[-1::-1])
print()

# Limited Rows selection using column
print(df.iloc[0:3, 0:2])
print()
print(df['name'].head(3))   #head() method is used to quickly view the first few rows of a Series or Dataframe
print(type((df['name'].head(3))))   #Print a Series by single bracket
print()
print(df[['name','city']].head(3))
print(type((df[['name','city']].head(3))))  #Print a DataFrame by double bracket
print()
print(df[['city','name']].iloc[:3])
print()

# Drop rows from a DataFrame based on certain condition applied on a DataFrame
result = df[df['city'] != 'Delhi']  #Drop rows where column city contains Delhi
print(result)
print()
result = df.drop(df[df['age'] <= 30].index)
print(result)
print()
''' .index gives you row labels.
Used in df.drop() to specify which rows to delete.'''

# Insert row at given position using python dataframe
frame_to_list = df.values.tolist()
print(frame_to_list)
print()
frame_to_list.insert(3,['Charu', 21, 'Jaipur']) #Here 3 is the 3rd index of list
df_result = pd.DataFrame(frame_to_list, columns=df.columns) #Making DataFrame from list
print(df_result)
print()

new_row = pd.DataFrame({'name':['Charu'],'age':[21],'city':['Jaipur']})
df_result = pd.concat([df.iloc[:2], new_row, df.iloc[2:]], ignore_index=True)
# here df.iloc[:2] indicate before index 2 and df.iloc[2:] indicates after index 2 i.e. new_row is at index 2
print(df_result)
print()

# Create a List from rows in Python DataFrame
print(df.values.tolist())   #Prints a list of lists, Column label is not preserved here

