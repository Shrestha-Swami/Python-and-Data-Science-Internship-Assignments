import pandas as pd

'''
1) Explore more regex patterns
eg. The Regex pattern used to validate email addresses, mobile no, string and more
'''

# Extracts digits from price strings
df = pd.DataFrame({'price': ['$23.99', 'USD 450.00', 'INR 3,000']})
df['clean_price'] = df['price'].str.replace(r'[^\d.]', '', regex=True).astype(float)
# Extracts digits and decimal point and adds a new column clean_price with floating values
# regex=True treats a literal as a regular expression
print(df)
print()

# Extract Email From Text
df = pd.DataFrame({'info': ['Contact me at abc@gmail.com or call me', 'Reach out: hello@domain.org']})
df['email'] = df['info'].str.extract(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
#Extracts the first email address in the string
print(df)
print()

# Remove Special Characters (Keep Alphanumerics)
df = pd.DataFrame({'text': ['Hello!!', '123@#$', 'Good_Morning']})
df['clean'] = df['text'].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
#Removes everything except letters and numbers
print(df)
print()

# Extract Indian phone number
df = pd.DataFrame({
    'text': [
        'Call at +91 9876543210',      # valid
        'Reach me at +91-8123456789',  # valid
        'Use +91 5123456789',          # invalid (starts with 5)
        'My number is +919234567890',  # valid
        'Emergency: +91 1234567890'    # invalid (starts with 1)
    ]
})

# Extract valid +91 phone numbers starting with 6-9
df['phone'] = df['text'].str.extract(r'(\+91[\s-]?[6-9]\d{9})')
print(df)
print()

# Extract Year From Text
df = pd.DataFrame({'text': ['Founded in 1998', 'Since 2005', 'Established: 2010']})
df['year'] = df['text'].str.extract(r'(\d{4})')
#Extracts 4-digit year
print(df)
print()

# Extract Hashtags from Social Posts
df = pd.DataFrame({'post': ['Loving #Python and #AI', 'Working on #ML']})
df['hashtags'] = df['post'].str.findall(r'#\w+')
print(df)
print()

'''
Explore more datetime functions and uses in pandas
'''

data = {
    'order_id': ['A101', 'A102', 'A103', 'A104', 'A105', 'A106'],
    'order_date': ['2023-01-01', '2023-02-15', '2023-03-05', '2023-06-25', '2023-07-15', 'Invalid Date'],
    'amount': [500, 700, 650, 800, 950, 1000]
}

df = pd.DataFrame(data)
print(df)
print()

# Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
print(df)
print()
'''When you use pd.to_datetime() to convert a column (or list) of date strings into datetime
 objects, errors='coerce' tells pandas to:
“If a value cannot be parsed as a valid date, don’t throw an error — just convert it to 
NaT (Not a Time).”'''

# Extract Components
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['day'] = df['order_date'].dt.day
df['weekday'] = df['order_date'].dt.day_name()
print(df['year'])
print()
print(df['month'])
print()
print(df['day'])
print()
print(df['weekday'])
print()

# Add/Subtract Time
df['delivery_date'] = df['order_date'] + pd.Timedelta(days=5)
print(df['delivery_date'])
print()
df['days_since_order'] = pd.Timestamp('2023-12-31') - df['order_date']
print(df['days_since_order'])
print()

# Format Dates
df['formatted_date'] = df['order_date'].dt.strftime('%d-%b-%Y')
print(df['formatted_date'])
print()

# Handle Missing dates
print(df['order_date'].isna())

# Set order_date as Index & Resample
df.set_index('order_date', inplace=True)
monthly_sales = df.resample('ME').sum(numeric_only=True)
print("\nFull Dataset After Date Operations:")
print(df.to_string())

print("\nMonthly Sales Summary:")
print(monthly_sales)


'''import matplotlib.pyplot as plt

monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.ylabel("Amount")
plt.show()'''
