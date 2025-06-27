import pandas as pd

df = pd.read_csv('people.csv')
print("Person DataFrame is: ")
print(df.to_string())
print()

# To print start 10 rows
print(df.head(10).to_string())
print()
# To print last 10 rows
print(df.tail(10).to_string())
print()
# Get a summary of the dataframe
print(df.info())
print()
# Generate descriptive statistics for numerical columns
print(df.describe())
print()
# Check the dimensions of dataframe
print(df.shape)
print()
# For the name of columns
print(df.columns)
print()
# Perform basic analysis of specific column
print(df['First Name'])
print()
# Filter data based on a condition
print(df[df['Index'] < 11].head(10))
print()

print("Grouping by job title with index values and then finding the mean, sum and count: ")
group_data = df.groupby('Job Title')['Index'].agg(['mean','sum','count'])
print(group_data.to_string())
print()

print("Grouping data on the basis of sex and their total count: ")
# Method1
group_data = df.groupby('Sex')['Index'].count()
print(group_data)
print()
#Method2
print(df['Sex'].value_counts())

new_df = df.dropna()
print(new_df.to_string())   #It doesn't remove the null values from original dataframe
print()

x = df['Index'].median()
df.fillna(x, inplace=True)
print(df.head(10).to_string())

'''df.fillna(0, inplace=True)      #Fills null values with 0
print(df.to_string())
print()'''
'''df.dropna(inplace=True)     #remove all rows containing null values from dataframe
print(df.to_string())
print()'''

df['First Name'] = df['First Name'].str.strip().str.title()
print(df['First Name'].to_string())
'''.str.strip()
    This removes leading and trailing whitespace (spaces, tabs, newlines) from each name.
    .str.title()
    This converts each name to title case, meaning the first letter is capitalized, and all 
    others are lowercase.
'''
