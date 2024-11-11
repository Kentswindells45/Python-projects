import tkinter
from tkinter import *
# to import tkinter font you need to call it and name it with a variable
import tkinter.font as tkFont

display = tkinter.Tk()
display.title("CALCULATOR")
display.iconbitmap("E:/UI")
display.resizable("false", "false")
display.geometry("500x500")


def number(num):
    current_value = screen.get()
    screen.delete(0, END)
    screen.insert(0, current_value + num)


def clear():
    screen.delete(0, END)


# use a variable(fontStyle)or other to contain the tkinter fonts.

fontStyle = tkFont.Font(family="Italic", size=18)
screen = Entry(font=fontStyle, width=50, bd=5)
c = Button(command=clear, text="C", width=5, font=fontStyle, fg="Black", bg="Gray")
m = Button(text="%", width=5, font=fontStyle, fg="Black", bg="Gray")
d = Button(text="/", width=5, font=fontStyle, fg="Black", bg="Gray")
e = Button(command=lambda: number("8"), text="8", width=5, font=fontStyle, fg="Black", bg="Gray")
n = Button(command=lambda: number("9"), text="9", width=5, font=fontStyle, fg="Black", bg="Gray")
multiply = Button(text="*", width=5, font=fontStyle, fg="Black", bg="Gray")
s = Button(command=lambda: number("6"), text="6", width=5, font=fontStyle, fg="Black", bg="Gray")
p = Button(command=lambda: number("7"), text="7", width=5, font=fontStyle, fg="Black", bg="Gray")
mi = Button(text="-", width=5, font=fontStyle, fg="Black", bg="Gray")
f = Button(command=lambda: number("4"), text="4", width=5, font=fontStyle, fg="Black", bg="Gray")
v = Button(command=lambda: number("5"), text="5", width=5, font=fontStyle, fg="Black", bg="Gray")
pl = Button(text="+", width=5, font=fontStyle, fg="Black", bg="Gray")
t = Button(command=lambda: number("2"), text="2", width=5, font=fontStyle, fg="Black", bg="Gray")
th = Button(command=lambda: number("3"), text="3", width=5, font=fontStyle, fg="Black", bg="Gray")
point = Button(text=".", width=5, font=fontStyle, fg="Black", bg="Gray")
z = Button(command=lambda: number("0"), text="0", width=5, font=fontStyle, fg="Black", bg="Gray")
o = Button(command=lambda: number("1"), text="1", width=5, font=fontStyle, fg="Black", bg="Gray")
equals = Button(text="=", width=5, font=fontStyle, fg="Black", bg="Brown")

screen.grid(row=0, column=0, columnspan=10)
c.grid(row=5, column=0)
m.grid(row=5, column=1)
d.grid(row=5, column=3)
e.grid(row=6, column=0)
n.grid(row=6, column=1)
multiply.grid(row=6, column=3)
s.grid(row=7, column=0)
p.grid(row=7, column=1)
mi.grid(row=7, column=3)
f.grid(row=8, column=0)
v.grid(row=8, column=1)
pl.grid(row=8, column=3)
t.grid(row=9, column=0)
th.grid(row=9, column=1)
point.grid(row=9, column=3)
z.grid(row=10, column=0)
o.grid(row=10, column=1)
equals.grid(row=10, column=3)
display.mainloop()
