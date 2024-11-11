import tkinter
from tkinter import *
import tkinter.font as TKFont

display = tkinter.Tk()
display.title("Login Page")
display.iconbitmap("E:/UI")
display.resizable("false", "false")
display.geometry("310x300")


def Reset():
    user_txt.delete(0, END)
    pas_txt.delete(0, END)


fontStyle = TKFont.Font(family="Helvetica", size=18)
fontStyle_2 = TKFont.Font(family="Italic", size=18)

user_name = Label(text="User Name:", font=fontStyle)
user_txt = Entry(justify="right", font=fontStyle, width=12, bg="White", fg="Black")
password = Label(text="Password:", font=fontStyle)
pas_txt = Entry(justify="right", font=fontStyle, width=12, bg="White", fg="Black")
btn = Button(text="LOGIN", font=fontStyle, bg="Yellow", fg="Black")
btn_2 = Button(command=Reset, text="RESET", font=fontStyle, bg="Pink", fg="Black")

user_name.grid(row=0, column=0, pady=5)
user_txt.grid(row=2, column=0, pady=5)
password.grid(row=3, column=0, pady=5)
pas_txt.grid(row=4, column=0, pady=5)
btn.grid(row=5, column=0, pady=5)
btn_2.grid(row=5, column=1, pady=5)
display.mainloop()
