# call tkinter package
import tkinter
# below show how all library of tkinter by typing from tkinter import *
from tkinter import *

# name a variable ( window)
# create a blank space
window = tkinter.Tk()
# show the window


# give a title
window.title("Welcome Screen")
# how to use icons you must first have an icon file extinction on your pc
window.iconbitmap("E:/UI")
# how to resize your window (the false,false means cant be resizable)
window.resizable("false", "false")
# the dimension where no one can resize it with letter (x)
window.geometry("800x500")
# runs the whole program
window.mainloop()
