import sqlite3

conn = sqlite3.connect('student.db')

conn.execute('''
CREATE TABLE student
(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    branch VARCHAR(100)
)
''')

conn.execute('''
CREATE TABLE marks
(
    id INTEGER PRIMARY KEY,
    subject VARCHAR(100),
    marks float
)
''')

conn.execute('''
CREATE TABLE courses
(
    id   INTEGER PRIMARY KEY,
    name VARCHAR(100)
)
''')

conn.close()