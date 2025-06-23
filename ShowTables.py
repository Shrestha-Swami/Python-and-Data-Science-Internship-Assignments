import sqlite3

conn = sqlite3.connect('student.db')
data = conn.execute('''Select * from student''')
print("Student Details")
for x in data:
    print(x)
print()
mark = conn.execute('''Select * from marks''')
print("Science Marks Details")
for x in mark:
    print(x)
print()
course = conn.execute('''Select * from courses''')
print("Course Details")
for x in course:
    print(x)