import pandas as pd

# 1)
# Create a Pandas Series from Dictionary
data_set = {
    'st_name': ['Anaya', 'Shreya', 'Maya'],
    'class': [8, 9, 7],
    'marks': [36, 40, 38]
}
sd = pd.Series(data_set)
print("Pandas Series from Dictionary:")
print(sd)
print(type(sd))
print()

# Create Pandas Series from Lists

data = [10,20,30,40,50]
sl = pd.Series(data, dtype=float, index=['a','b','c','d','e'])
print("Pandas Series from Lists:")
print(sl)
print(type(sl))
print()

# Access the elements of Series in Pandas
print(sl[['a','b','c']])
print()
print(sd.iloc[[0,2]])
print()
print(sl[sl>30])
print()
print(sd.loc[['st_name', 'marks']])
print()

# 2) DataFrames
# Make a Pandas DataFrame using 2-D List

data = [
    [1,'Anaya',30],
    [2,'Shreya',25],
    [3,'Maya',32],
    [4,'Kavya',34],
]
df = pd.DataFrame(data, columns=['id', 'name', 'age'])
print("Pandas DataFrame using 2-D List:")
print(df)
print(type(df))
print()

# Create DataFrame from Python Dictionary
data = {
    "Fruits": ["apple", "banana", "cherry"],
    "Weight_kg": [2, 3, 1],
    "Price": [200.00, 50.00, 100.00]
}
df = pd.DataFrame(data, index=[1,2,3])
print("DataFrame from Python Dictionary:")
print(df)
print()

# Create DataFrame using list of Lists
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
df = pd.DataFrame(data, columns=['c1', 'c2', 'c3'])
print("Pandas DataFrame using List of Lists:")
print(df)
print()

# Create a Pandas DataFrame using list of Tuples
data = [
    ('Anaya', 30),
    ('Shreya', 25),
    ('Maya', 32)
]
df = pd.DataFrame(data, columns=['name', 'age'], index=[1,2,3])
print("Pandas DataFrame using List of Tuples:")
print(df)
print()

# Create Pandas DataFrame using List of Dictionaries
data = [
    {'fruit': 'apple', 'weight_kg': 3, 'price': 200},
    {'fruit': 'banana', 'weight_kg': 4, 'price': 50},
    {'fruit': 'cherry', 'weight_kg': 1, 'price': 200}
]
df = pd.DataFrame(data)
print("Pandas DataFrame using List of Dictionaries:")
print(df)
print()