import sqlite3

# dbase = sqlite3.connect("School.db")
# dbase.execute('''CREATE TABLE  IF NOT EXISTS student(ID INT PRIMARY KEY, FIRSTNAME TEXT, LASTNAME TEXT,
# ADDRESS TEXT, DOB DATE)''')

dbase = sqlite3.connect("Teachers.db")
# dbase.execute('''CREATE TABLE  IF NOT EXISTS student (ID INT PRIMARY KEY,FIRSTNAME TEXT, LASTNAME TEXT)''')


dbase.execute('''INSERT INTO Teachers(ID, FIRSTNAME, LASTNAME) VALUES(5, 'KENT', 'FOX' )''')
dbase.commit()

dbase.close()
