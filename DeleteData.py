import sqlite3
conn = sqlite3.connect('student.db')
id = input('Enter ID to delete: ')
if id.isdigit():
    data = conn.execute("DELETE FROM courses WHERE id =" + id)
    conn.commit()
    print("Course Details after deletion of course of id = " + id)

    if data.rowcount == 0:
        print(f"No course found with id = {id}. Nothing was deleted.")
    else:
        print(f"Course with id = {id} deleted successfully.")

else:
    print("Invalid ID. Please enter a numeric value.")

data = conn.execute("SELECT * FROM courses")
for x in data:
    print(x)
conn.close()