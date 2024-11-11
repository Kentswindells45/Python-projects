import tkinter
from tkinter import *
import tkinter.font as lk_font
from tkinter import messagebox

main_screen = tkinter.Tk()
main_screen.title("Kent Revolution")
main_screen.iconbitmap("E:/UI")
main_screen.resizable("true", "true")
main_screen.geometry("300x300")
main_screen.eval("tk::PlaceWindow . center")

font_style = lk_font.Font(family="times and romans", size=15)
font_style_2 = lk_font.Font(family="Helvetica", size=15)

sign_in = Label(text="Kent Revolution", font=font_style, fg="Brown")
name = Label(text="Name :", font=font_style_2, fg="Blue")
txt_name = Entry(font=font_style, fg="Green")
ocp = Label(text="Role : ", font=font_style_2, fg="Blue")
ocpt = Entry(font=font_style, fg="Green")
num = Label(text="Items :", font=font_style_2, fg="Blue")
numb = Entry(font=font_style, fg="Green")

sign_in.grid(row=0, column=0, columnspan=2, pady=5)
name.grid(row=1, column=0, pady=5)
txt_name.grid(row=1, column=1, pady=5)
ocp.grid(row=2, column=0, pady=5)
ocpt.grid(row=2, column=1, pady=5)
num.grid(row=3, column=0, pady=5)
numb.grid(row=3, column=1, pady=5)
main_screen.mainloop()
