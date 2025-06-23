import sqlite3

conn = sqlite3.connect('student.db')

conn.execute('''
INSERT INTO student values(101, 'Ajay', 20, 'CSE')
''')
conn.execute('''
INSERT INTO student values(102, 'Vijay', 20, 'EE')
''')
conn.execute('''
INSERT INTO student values(103, 'Jay', 20, 'ME')
''')
conn.execute('''
INSERT INTO student values(104, 'Sanjay', 20, 'CE')
''')
conn.execute('''
INSERT INTO marks values(101, 'Science', 85.5)
''')
conn.execute('''
INSERT INTO marks values(102, 'Science', 90)
''')
conn.execute('''
INSERT INTO marks values(103, 'Science', 64.5)
''')
conn.execute('''
INSERT INTO marks values(104, 'Science', 92.4)
''')
conn.execute('''
INSERT INTO courses values(301, 'BTECH')
''')
conn.execute('''
INSERT INTO courses values(302, 'BARCH')
''')
conn.execute('''
INSERT INTO courses values(303, 'BCA')
''')
conn.execute('''
INSERT INTO courses values(304, 'BSc')
''')



conn.commit()
conn.close()