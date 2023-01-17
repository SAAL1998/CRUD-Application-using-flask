import sqlite3
c = sqlite3.connect("employeedetails.db")
print("database created successfully")
c.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")
c.close()