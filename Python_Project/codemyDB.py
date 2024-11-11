import tkinter
from tkinter import *
import sqlite3

root = Tk()
root.title("KentDB")
root.iconbitmap("E:/UI")
root.geometry("400x400")

# connect a database
conn = sqlite3.connect('address_book.db')

# Create a cursor object
c = conn.cursor()

# create table for database
c.execute("""CREATE TABLE IF NOT EXISTS addresses(
    
    first_name text,
    last_name text,
    address text,
    country text,
    city text,
    zipcode integer
    )""")

# comit changes
conn.commit()

# close connection
conn.close()

Last = Label(text="Last Name:", fg="Green").grid(row=0, column=0, columnspan=2, pady=1)

root.mainloop()
