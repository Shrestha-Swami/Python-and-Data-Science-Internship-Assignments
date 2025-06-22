"""
 In your last program where you find the total and percentage of a student's marks of 5 
 subject, find the grade of the student using conditional statement. E.g. grade 'A' if 
 percentage is greater than or equals to 60, 'B' for  percentage is greater than or equals 
 to 50 and less than 60,  'C' for  percentage is greater than or equals to 40 and less than 
 50,  'D' for  percentage is greater than or equals to 33 and less than 40, otherwise 'Fail'
"""

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
print(f"Your name is {name}, your class is {your_class} and your percentage is {percentage :.2f}%.")
if percentage >= 60:
    print("Your grade is A")
elif percentage >= 50 and not percentage >= 60:
    print("Your grade is B")
elif percentage >= 40 and not percentage >= 50:
    print("Your grade is C")
elif percentage >= 33 and not percentage >= 40:
    print("Your grade is D")
else:
    print("You are failed")



"""Input a number from user and find its factorial using for loop"""

n = int(input("Enter a number to find its factorial: "))
fact = 1
for i in range(1, n + 1):
        fact = fact * i
print("The factorial of", n, "is", fact)

"""
Create a billing program using list. Program should have options to 
1. Create Bill
2. Display Item Price and total bill amount
3. Display Total
4. Exit
"""

price = []
total_bill = 0

while True:
    print('''
    1. Create Bill
    2. Display Item Price and total bill amount
    3. Display Total
    4. Exit
    ''')
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Creating Bill. Enter item prices one by one. Type 'stop' to finish.")
        price.clear()
        total_bill = 0
        while True:
            item = input("Enter item price or type 'stop': ")
            if item.lower() == 'stop':
                break
            item_price = float(item)
            price.append(item_price)
            total_bill += item_price

    elif choice == 2:
        if price:
            print("Item prices:")
            # enumerate gives index and value, starting from 1
            # for i, p in enumerate(price, 1):
            #     print(f"Item {i}: {p}")

            for i in range(len(price)): #Other way instead of using enumerate function
                print(f"Item {i + 1}: {price[i]}")

            print("Total bill is: ", total_bill)
        else:
            print("No items in the bill yet.")

    elif choice == 3:
        print("Total bill is: ", total_bill)

    elif choice == 4:
        print("Exited from loop")
        break

    else:
        print("Invalid choice (Choose between 1 to 4)")

"""
Write a  Python program to find the smallest number in a list.
Write a  Python program to find the second greatest number in a list.
Write a  Python program to find the second smallest number in a list.
"""

n = int(input("Enter the length of list: "))
if n < 2:
    print("List must contain at least two elements.")
else:
    lst = []
    for i in range(n):
        lst.append(int(input(f"Enter item {i + 1}: ")))
    print("List =", lst)

    # To find the smallest number in list
    smallest_num = lst[0]
    for i in range(1, n):
        if lst[i] < smallest_num:
            smallest_num = lst[i]
    print(f"The smallest number in the list is: {smallest_num}")

    # To find the second greatest number
    greatest_num = float('-inf')
    second_greatest_num = float('-inf')
    for i in range(n):
        if lst[i] > greatest_num:
            second_greatest_num = greatest_num
            greatest_num = lst[i]
        elif lst[i] > second_greatest_num and lst[i] != greatest_num:
            second_greatest_num = lst[i]

    if second_greatest_num == float('-inf'):
        print("There is no second greatest number (all elements may be the same).")
    else:
        print(f"The second greatest number in the list is: {second_greatest_num}")

    # To find the second smallest number
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for i in range(n):
        if lst[i] < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = lst[i]
        elif lst[i] < second_smallest_num and lst[i] != smallest_num:
            second_smallest_num = lst[i]

    if second_smallest_num == float('inf'):
        print("There is no second smallest number (all elements may be the same).")
    else:
        print(f"The second smallest number in the list is: {second_smallest_num}")
