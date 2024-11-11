import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3

# database connection
create_db = sqlite3.connect("College_form.db")
c = create_db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS applicants(
    applicant_first_Name text,
    last_Name text,
    email text PRIMARY KEY,
    gender text,
    contact text  
      )""")

create_db.close()

screen = tkinter.Tk()
screen.title("Collage Forms")
screen.iconbitmap("E:/UI")
screen.resizable("false", "false")
screen.geometry("300x340")
screen.eval("tk::PlaceWindow . center")

options = [
    "Ethical Hacking",
    "Software Dev.",
    "Graphics",
    "Networking",
    "Robotics",
    "MS Office"
]

qVar = StringVar()
qVar.set(options[0])

genVar = StringVar()
genVar.set("Select Gender")


def CloseWindow():
    response = messagebox.askquestion("prompt", "Do you want to close window?")
    if response == "yes":
        screen.destroy()


font_style = tkFont.Font(family="Corbel", size=15)
font_style_2 = tkFont.Font(family="Helvetica", size=10)

title = Label(text="College Form Portal", font=font_style, fg="Orange").grid(row=0, column=0, columnspan=2, pady=5)
name = Label(text="First Name:", font=font_style, fg="Blue").grid(row=1, column=0, pady=5)
txt_name = Entry(font=font_style_2, width=15, bd=3).grid(row=1, column=1, pady=5)
Last = Label(text="Last Name:", font=font_style, fg="Blue").grid(row=2, column=0, pady=5)
txt_last = Entry(font=font_style_2, width=15, bd=3).grid(row=2, column=1, pady=5)
gender = Label(text="Gender", font=font_style, fg="Blue").grid(row=3, column=0, pady=5)
txt_gender = OptionMenu(screen, genVar, "Male", "Female", "Rather not say").grid(row=3, column=1, pady=5)
email = Label(text="Email:", font=font_style, fg="Blue").grid(row=4, column=0, pady=5)
txt_email = Entry(font=font_style_2, width=15, bd=3).grid(row=4, column=1, pady=5)
contact = Label(text="Contact", font=font_style, fg="Blue").grid(row=5, column=0, pady=5)
txt_contact = Entry(font=font_style_2, width=15, bd=3).grid(row=5, column=1, pady=5)
qualification = Label(text="Course:", font=font_style, fg="Blue").grid(row=6, column=0, pady=5)
txt_course = OptionMenu(screen, qVar, *options).grid(row=6, column=1, pady=5)

# txt_course = Entry(font=font_style_2, width=15)
sign = Button(text="Submit", font=font_style, fg="Green", bd=4).grid(row=7, column=0, pady=5)
cancel = Button(command=CloseWindow, text="Cancel", font=font_style, fg="Red", bd=4).grid(row=7, column=1, pady=5)

screen.mainloop()
