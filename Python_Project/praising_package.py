import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.font as mk_Font

main_window = tkinter.Tk()
main_window.title("Kent")
main_window.iconbitmap("E:/UI")
main_window.configure(background="red")
main_window.resizable("false", "false")
main_window.geometry("360x320")
main_window.eval("tk::PlaceWindow . center")
font_1 = mk_Font.Font(family="Corbel", size=12)

title = Label(text="Welcome To Kent Corp (c) 2021", font=font_1, fg="Green")
title.grid(row=0, column=0, columnspan=2, pady=5)
name = Label(text=" Name:", font=font_1, fg="Brown")
name.grid(row=1, column=0, pady=5)

main_window.mainloop()