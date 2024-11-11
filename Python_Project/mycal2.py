import tkinter
from tkinter import *
import tkinter.font as mk_font

my_cal = tkinter.Tk()
my_cal.title("Cal")
my_cal.resizable("true", "true")
my_cal.iconbitmap("E:/UI")
my_cal.geometry("260x309")
my_cal.eval("tk::PlaceWindow . center")


def number(num):
    current_value = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current_value) + num)
    Screen_Data = data.get()
    data.delete(0, END)
    data.insert(0, str(Screen_Data) + num)


def clear():
    screen.delete(0, 1)
    data.delete(0, 1)


# add
def sum():
    first_num = screen.get()
    global fnum
    global opt
    data.delete(0, END)
    data.insert(0, first_num + "+")
    opt = "add"
    fnum = first_num
    screen.delete(0, END)


def product():
    first_num = screen.get()
    global fnum
    global opt
    data.delete(0, END)
    data.insert(0, first_num + "*")
    opt = "multiply"
    fnum = first_num
    screen.delete(0, END)


def difference():
    first_num = screen.get()
    global fnum
    global opt
    data.delete(0, END)
    data.insert(0, first_num + "-")
    opt = "subtract"
    fnum = first_num
    screen.delete(0, END)


def divide():
    first_num = screen.get()
    global fnum
    global opt
    data.delete(0, END)
    data.insert(0, first_num + "/")
    opt = "divide"
    fnum = first_num
    screen.delete(0, END)


def percent():
    first_num = screen.get()
    global fnum
    global opt
    data.delete(0, END)
    data.insert(0, first_num + "%")
    opt = "percent"
    fnum = first_num
    screen.delete(0, END)


# equal to def
fnum = 0


def equal():
    second_num = screen.get()
    screen.delete(0, END)
    if fnum and second_num != "":
        if opt == "add":
            screen.insert(0, int(fnum) + int(second_num))
        if opt == "multiply":
            screen.insert(0, int(fnum) * int(second_num))
        if opt == "subtract":
            screen.insert(0, int(fnum) - int(second_num))
        if opt == "divide":
            screen.insert(0, int(fnum) // int(second_num))
        if opt == "percent":
            screen.insert(0, float(fnum) % float(second_num))


fontStyle = mk_font.Font(family="Helvetica", size=15)
fontStyle_2 = mk_font.Font(family="Italic", size=15)
data = Entry(justify="right", width=16, font=fontStyle_2, bg="White")
screen = Entry(justify="right", width=16, font=fontStyle_2, bg="White")
clear = Button(justify="right", command=clear, text="C", width=7, font=fontStyle, bg="Pink", fg="Black")
percentage = Button(command=percent, text="%", width=7, font=fontStyle, bg="Pink", fg="Black")
division = Button(command=divide, text="/", width=7, font=fontStyle, bg="Pink", fg="Black")
eight = Button(command=lambda: number("8"), text="8", width=7, font=fontStyle, bg="Pink", fg="Black")
nine = Button(command=lambda: number("9"), text="9", width=7, font=fontStyle, bg="Pink", fg="Black")
multi = Button(command=product, text="*", width=7, font=fontStyle, bg="Pink", fg="Black")
six = Button(command=lambda: number("6"), text="6", width=7, font=fontStyle, bg="Pink", fg="Black")
seven = Button(command=lambda: number("7"), text="7", width=7, font=fontStyle, bg="Pink", fg="Black")
subtract = Button(command=difference, text="-", width=7, font=fontStyle, bg="Pink", fg="Black")
five = Button(command=lambda: number("5"), text="5", width=7, font=fontStyle, bg="Pink", fg="Black")
four = Button(command=lambda: number("4"), text="4", width=7, font=fontStyle, bg="Pink", fg="Black")
add = Button(command=sum, text="+", width=7, font=fontStyle, bg="Pink", fg="Black")
two = Button(command=lambda: number("2"), text="2", width=7, font=fontStyle, bg="Pink", fg="Black")
three = Button(command=lambda: number("3"), text="3", width=7, font=fontStyle, bg="Pink", fg="Black")
point = Button(command=lambda: number("."), text=".", width=7, font=fontStyle, bg="Pink", fg="Black")
zero = Button(command=lambda: number("0"), text="0", width=7, font=fontStyle, bg="Pink", fg="Black")
one = Button(command=lambda: number("1"), text="1", width=7, font=fontStyle, bg="Pink", fg="Black")
equals_to = Button(comman=equal, text="=", width=7, font=fontStyle, bg="Pink", fg="Black")

data.grid(row=0, column=0, columnspan=10)
screen.grid(row=1, column=0, columnspan=10)
clear.grid(row=7, column=0)
percentage.grid(row=7, column=1)
division.grid(row=7, column=3)
eight.grid(row=8, column=0)
nine.grid(row=8, column=1)
multi.grid(row=8, column=3)
six.grid(row=9, column=0)
seven.grid(row=9, column=1)
subtract.grid(row=9, column=3)
five.grid(row=10, column=0)
four.grid(row=10, column=1)
add.grid(row=10, column=3)
two.grid(row=11, column=0)
three.grid(row=11, column=1)
point.grid(row=11, column=3)
zero.grid(row=12, column=0)
one.grid(row=12, column=1)
equals_to.grid(row=12, column=3)

my_cal.mainloop()
