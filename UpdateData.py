import sqlite3
conn = sqlite3.connect('student.db')
conn.execute("Update student set name = 'Abhay' where id = 103")
conn.execute("Update student set age = 19 where id = 102")
conn.execute("Update student set age = 22 where id = 103")
conn.execute("Update student set age = 21 where id = 104")
print("Student Details after Updation")
data = conn.execute("SELECT * FROM student order by age")
for x in data:
    print(x)
print()
conn.execute("Update marks set marks = 70.5 where id = 103")
print("Marks Details after Updation")
marks = conn.execute("SELECT * FROM marks order by marks desc")
for x in marks:
    print(x)

conn.commit()
conn.close()