"""
Write a function for basic math operations like add, subtract, multiply, divide and use
this in your program, take 2 number input from user.
"""

# Addition
def add(num1, num2):
    return num1 + num2

# Subtraction
def subtract(num1, num2):
    return num1 - num2

# Multiplication
def multiply(num1, num2):
    return num1 * num2

# Division
def divide(num1, num2):
    return num1 / num2


n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
print(f"The sum of {n1} and {n2} is {add(n1, n2)}")
print(f"The difference of {n1} and {n2} is {subtract(n1, n2)}")
print(f"The product of {n1} and {n2} is {multiply(n1, n2)}")
print(f"The quotient {n1} and {n2} is {divide(n1, n2)}")


# Write a program to check Palindrome number

def isPalindrome(num):
    original = num
    rev = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        rev = (rev * 10) + rem
    if original == rev:
        return True
    else:
        return False
    # or simply return n == rev instead of True and False

n = int(input("Enter the number to check whether it is palindrome or not: "))
if isPalindrome(n):
    print(n, "is a palindrome number.")
else:
    print(n, "is not a palindrome number.")