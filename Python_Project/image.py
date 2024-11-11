from tkinter import *

window = Tk()
window.title("Kent image")
window = Canvas(window, width=450, height=450)
window.pack()

image = PhotoImage(file="E:\\PS4\\SHARE\\Screenshots\\fifa21.png")
window.create_image(0, 0, anchor=NW)
