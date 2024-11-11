import tkinter
from tkinter import *
import tkinter.font as mk_font
from tkinter import messagebox
import sqlite3

pj64 = Tk()
pj64.title("Project_64")
pj64.iconbitmap("E:/UI")
pj64.resizable("false", "false")
pj64.geometry("250x100")
pj64.eval("tk::PlaceWindow . center")

font1 = mk_font.Font(family="corbel", size=18)

intro_screen = Label(pj64, text="Welcome To Project 64", font=font1, fg="Brown")
intro_screen.pack(pady=20)


def main_page():
    pj64.destroy()
    main_win = Tk()
    main_win.title("main screen")
    main_win.geometry("360x320")
    main_win.resizable("false", "false")
    main_win.eval("tk::PlaceWindow . center")

    mmk = Label(main_win, text="Project 64 presents", font=font1, fg="Blue")
    mmk.grid(row=0, column=0, columnspan=2, pady=5)
    lab = Label(main_win, text="Project 64 provides the following", font=("Helvetica", 18))
    lab.grid(row=0, column=1, pady=5)


pj64.after(3000, main_page)

pj64.mainloop()
