import tkinter
from tkinter import *
import tkinter.font as mk_font

graphic = tkinter.Tk()
graphic.title("Sign In Facebook")
graphic.iconbitmap("E:/UI")
graphic.resizable("false", "false")
graphic.geometry("350x300")


def clear():
    text_f_name.delete(0, END)
    text_l_name.delete(0, END)
    text_u_name.delete(0, END)
    text_pas.delete(0, END)


FontStyle = mk_font.Font(family="Helvetica", size=15, )
register = Label(text="Sign in", font=FontStyle, fg="Blue")
first_name = Label(text="First Name:", font=FontStyle, fg="Blue")
text_f_name = Entry(font=FontStyle, width=15, fg="Black")
Last_name = Label(text="Last Name:", font=FontStyle, fg="Blue")
text_l_name = Entry(font=FontStyle, width=15, fg="Black")
U_name = Label(text="User Name:", font=FontStyle, fg="Blue")
text_u_name = Entry(font=FontStyle, width=15, fg="Black")
pas = Label(text="Password:", font=FontStyle, fg="Blue")
text_pas = Entry(font=FontStyle, width=15, fg="Black")
bt_sign = Button(text="Sign In", font=FontStyle, fg="Blue")
bt_cancel = Button(command=clear, text="Cancel", font=FontStyle, fg="Blue")

first_name.grid(row=1, column=0, pady=5)
text_f_name.grid(row=1, column=1, pady=5)
Last_name.grid(row=2, column=0, pady=5)
text_l_name.grid(row=2, column=1, pady=5)
U_name.grid(row=3, column=0, pady=5)
text_u_name.grid(row=3, column=1, pady=5)
pas.grid(row=4, column=0, pady=5)
text_pas.grid(row=4, column=1, pady=5)
bt_sign.grid(row=5, column=0, pady=10)
bt_cancel.grid(row=5, column=1, pady=10)
register.grid(row=0, column=0, columnspan=2, pady=5)
graphic.mainloop()
