import sqlite3

conn = sqlite3.connect('student.db')
print("Students whose name startswith A: ")
data = conn.execute("SELECT * FROM student where name like 'A%'")
for row in data:
    print(row)
print()

print("Id and marks of those students whose marks in Science are greater than or equal to 90: ")
data = conn.execute("SELECT * FROM marks WHERE marks >= 90")
for row in data:
    print(row)
print()

print("Students Details after joining with marks table: ")
data = conn.execute('''
SELECT student.name, marks.subject, marks.marks
FROM student
JOIN marks ON student.id = marks.id
order by marks desc
''')
for row in data:
    print(row)
print()

avg_marks = conn.execute("SELECT AVG(marks) FROM marks WHERE subject = 'Science'")
for row in avg_marks:
    print("Average Science Marks:", row[0])
print()

cnt = conn.execute("SELECT COUNT(*) from student")
for row in cnt:
    print("Total Students:", row[0])
print()

dist_branch = conn.execute("SELECT DISTINCT branch FROM student")
for row in dist_branch:
    print("Branch:", row[0])
print()

cursor = conn.execute("SELECT * FROM student LIMIT 2")
for row in cursor:
    print(row)


