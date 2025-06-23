# Use print function to print strings

str1 = "Hello World"
print(str1)
print(type(str1))
print(str1[0:5])
print(str1[-1::-1]) #Reverse the string by slicing
name = input("Enter your name: ")
print("Hello " + name)
name = input("Enter your name: ")
your_class = int(input("Enter your class: "))
print("Your name is ",name, ", and you are in class ",your_class)
# By string formatting
name = input("Enter your name: ")
your_class = int(input("Enter your class: "))
print(f"Your name is {name}, and you are in class {your_class}")

# Write a simple basic calculator program in python
"""It should be dynamic where it should accept 2 inputs from the users and perform the following:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum of {num1} and {num2} is {num1 + num2}")
print(f"The difference of {num1} and {num2} is {num1 - num2}")
print(f"The product of {num1} and {num2} is {num1 * num2}")
print(f"The quotient of {num1} and {num2} is {num1 / num2}")
print(f"The remainder of {num1} and {num2} is {num1 % num2}")