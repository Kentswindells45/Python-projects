import tkinter
from tkinter import*
import tkinter.font as tkfont
from tkinter import messagebox
import sqlite3

root = tkinter.Tk()
root.title("KENT CORP___(c)")
root.iconbitmap("E:/UI")
root.resizable("false", "false")
root.geometry("360x300")
root.eval("tk::PlaceWindow . center")

gen = [
    "Male",
    "Female",
    "Other",
    "Specify"
]
genID = StringVar()
genID.set(gen[0])
genID.set("Select gender")

font1 = tkfont.Font(family="Corbel", size=15)

Lab = Label(text="Welcome To Kent Corp 2021(c)", font=font1, fg="Blue")
Lab.grid(row=0, column=0, columnspan=2, pady=5)
nam = Label(text="Name:", font=font1, fg="Brown")
nam.grid(row=1, column=0, pady=5)
txt_nam = Entry(font=font1, width=15, bd=5)
txt_nam.grid(row=1, column=1, pady=5)
user_name = Label(text="User Name:", font=font1, fg="Brown")
user_name.grid(row=2, column=0, pady=5)
txt_user_name = Entry(font=font1, width=15, bd=5)
txt_user_name.grid(row=2, column=1, pady=5)
gender = Label(text="Gender:", font=font1, fg="Brown")
gender.grid(row=3, column=0, pady=5)
text_gen =OptionMenu(root, genID, *gen)
text_gen.grid(row=3, column=1, pady=5)
cont = Label(text="Contact:", font=font1, fg="Brown")
cont.grid(row=4,column=0, pady=5)
txt_cont = Entry(font=font1, width=15, border=5)
txt_cont.grid(row=4, column=1, pady=5)


root.mainloop()