import tkinter
from tkinter import *
import tkinter.font as mk_font
from tkinter import messagebox
import sqlite3

kent_inc = "Kent Inc 2022(c)"

database = sqlite3.connect("Exhibition_new_era.db")
cur = database.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS clients(
      client's_name txt,
      Residence text,
      Gender text,
      Contact primary key)
""")
database.commit()
database.close()

root = tkinter.Tk()
root.title("Exhibition of new Era")
root.resizable("false", "false")
root.iconbitmap("E:/UI")
root.geometry("350x390")
