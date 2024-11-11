import tkinter
from tkinter import *
import tkinter.font as mk_font

graphic = tkinter.Tk()
graphic.title("My first Gui")
graphic.iconbitmap("E:/UI")
graphic.resizable("false", "false")
graphic.geometry("350x300")

L = Label(text='henry').pack()

graphic.mainloop()
