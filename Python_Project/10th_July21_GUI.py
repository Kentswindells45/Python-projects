import tkinter
from tkinter import *
# to import tkinter font you need to call it and name it with a variable
import tkinter.font as tkFont

display = tkinter.Tk()
display.title("Welcome Screen")
display.iconbitmap("E:/UI")
display.resizable("false", "false")
display.geometry("300x300")

# defining the component
# creating a diff font create another variable to change the font style
fontStyle = tkFont.Font(family="Italic", size=10)
welcome_text = Label(display, text="WELCOME TO GUI IN PYTHON", font=fontStyle)
SubMessage = Label(display, text="Let's started", font=fontStyle, fg="Red", bg="white")
txtName = Entry(font=fontStyle)
clickMe = Button(text="Submit")
# place allows you to place the object on your screen
# you can pack it when you want to increase the width
welcome_text.pack()
SubMessage.pack()
# txtName.place(x=60,y=50,height=40)
txtName.pack()
clickMe.pack()

display.mainloop()
