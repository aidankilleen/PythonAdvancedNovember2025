# database_intro.py


import sqlite3


conn = sqlite3.connect("member_database.db")
cursor = conn.cursor()

sql = "SELECT * FROM members"

rs = cursor.execute(sql)

for row in rs:
    print (row[1])
    print (row)

# sql = """
# CREATE TABLE IF NOT EXISTS members (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     active BOOLEAN NOT NULL
# );
# """
# cursor.execute(sql)
# conn.commit()



# sql = "INSERT INTO members (name, email, active) VALUES('Bob', 'bob@gmail.com', 1)"
# cursor.execute(sql)
# sql = "INSERT INTO members (name, email, active) VALUES('Carol', 'carol@gmail.com', 1)"
# cursor.execute(sql)
# sql = "INSERT INTO members (name, email, active) VALUES('Dan', 'dan@gmail.com', 1)"
# cursor.execute(sql)



#conn.commit()
conn.close()

