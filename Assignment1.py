"""Write a python program that takes in a student name, class. It should also take
 in five subject marks of the student and also find the total mark and percentage.
  Display a result in such a way that their name, class and percentage are printed."""

name = input("Enter your name: ")
your_class = int(input("Enter your class: "))
print("Enter the marks of the given 5 subjects(English, Hindi, Maths, Social Science,"
      " Science)")
english_marks = float(input("Enter your english marks: "))
hindi_marks = float(input("Enter your hindi marks: "))
maths_marks = float(input("Enter your maths marks: "))
social_science_marks = float(input("Enter your social science marks: "))
science_marks = float(input("Enter your science marks: "))
total_marks = english_marks + hindi_marks + maths_marks + social_science_marks + science_marks
print("Your total marks is: ", total_marks)
percentage = (total_marks / 500) * 100
print(f"Your name is {name}, your class is {your_class} and your percentage is {percentage}%.")


"""Input 2 strings concatenate them and store in another variable. Then perform generally 
used methods on it """

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str_cat = str1 + " " + str2
print(str_cat)
print(str_cat.capitalize())
print(str_cat.casefold())
print(str1.center(40, "-"))
print(str_cat.isalnum())
print(str_cat.isalpha())
print(str_cat.isdigit())
print(str_cat.islower())
print(str1.isspace())
print(str_cat.isupper())
print(str_cat.isprintable())
print(str_cat.isnumeric())
print(str2.istitle())
print(str1.lower())
print(str1.upper())

str1 = "Hello"
str2 = "World"

combined = str1 + str2
print("Concatenated String:", combined)

print("Uppercase:", combined.upper())
print("Lowercase:", combined.lower())
print("Swap Case:", combined.swapcase())
print("Title Case:", combined.title())
print("Capitalize:", combined.capitalize())
print("Length:", len(combined))
print("Is Alphabetic:", combined.isalpha())
print("Is Alphanumeric:", combined.isalnum())
print("Is Digit:", combined.isdigit())
print("Is Lowercase:", combined.islower())
print("Is Uppercase:", combined.isupper())
print("Is Title Case:", combined.istitle())
print("Starts with 'Hello':", combined.startswith("Hello"))
print("Ends with 'World':", combined.endswith("World"))
print("Count of 'l':", combined.count('l'))
print("Index of 'o':", combined.find('o'))
print("Last index of 'o':", combined.rfind('o'))
print("Replace 'World' with 'Universe':", combined.replace("World", "Universe"))
print("Split by 'o':", combined.split('o'))
print("Centered (width=20):", combined.center(20, '*'))
print("Left-justified (width=20):", combined.ljust(20, '-'))
print("Right-justified (width=20):", combined.rjust(20, '-'))
print("Stripped :", combined.strip())

words = ["Python", "is", "great"]
multiline_text = "Python\nJava\nC++"
tabbed_text = "Python\tis\tfun"
text = "Hello World"

# join() – join list of strings with a separator
joined = " ".join(words)
print("Joined:", joined)

# splitlines() – split string into list by line breaks
lines = multiline_text.splitlines()
print("Splitlines:", lines)

# partition() – splits the string at the first occurrence of separator
print("Partition result:", text.partition(" "))

# expandtabs() – replace tab characters with spaces
expanded = tabbed_text.expandtabs(4)
print("Expand Tabs:", expanded)

# maketrans() and translate() – map and replace characters
# can also enter two different strings inside maketrans to encode the string instead of dictionary
translation_table = str.maketrans({'H': 'J', 'o': '0'})
translated = text.translate(translation_table)
print("Translated:", translated)
