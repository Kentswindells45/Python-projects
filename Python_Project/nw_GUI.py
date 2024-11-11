import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3

window = tkinter.Tk()
window.title("My window")
window.iconbitmap("E:/UI")
window.resizable("false", "false")
window.geometry("250x340")
window.eval("tk::PlaceWindow . center")

sub = StringVar()
sub.set("Select Gender")

option = [
    " Youth President",
    "Vice President",
    "Youth Organizer",
    "Youth Secretary",
    "Prayer Secretary",
    "Finance Secretary",
    "Usher",
    "Member"
]
opt = StringVar()
opt.set(option[0])
opt.set("Select Position")

term = IntVar()


def New_Window():
    new = Toplevel()
    new.title("Sign In")
    new.resizable("false", "false")
    new.geometry("200x240")
    student_name = Label(new, text="Student Portal ", font=Font_style_2, fg="Blue").grid(row=0, column=0, columnspan=2)
    wel = Label(new, text="Welcome", fg="Green").grid(row=1, column=0, columnspan=2)
    details = Label(new, text="FULL DETAILS", fg="Brown").grid(row=2, column=0, columnspan=2)
    firstNam = Label(new, text="First Name :").grid(row=3, column=0)
    tfNam = Label(new, text=txt_name.get()).grid(row=3, column=1)
    u_name = Label(new, text="User Name :").grid(row=4, column=0)
    fn = Label(new, text=txt_username.get()).grid(row=4, column=1)
    user = Label(new, text="Contact :").grid(row=5, column=0)
    users = Label(new, text=txt_contact.get()).grid(row=5, column=1)
    pp = Label(new, text="Select Position :").grid(row=6, column=0)
    pas = Label(new, text=opt.get()).grid(row=6, column=1)
    gen = Label(new, text="Gender :").grid(row=7, column=0)
    mf = Label(new, text=sub.get()).grid(row=7, column=1)

    btclose = Button(new, command=new.destroy, text="LOG OUT").grid(row=8, column=0, columnspan=2)


def valid():
    if txt_name.get() == "" or txt_username.get() == "" or txt_pass.get() == "" or txt_contact.get() == "" or sub.get() == "Male" \
            or sub.get() == "Female":
        messagebox.showerror("Error", "Fill the blank spaces")
    else:
        New_Window()


def CloseWindow():
    response = messagebox.askquestion("Prompt", "Do you want to close this window?")
    if response == "yes":
        window.destroy()


Font_style = tkFont.Font(family="Helvetica", size=15)
Font_style_2 = tkFont.Font(family="Corbel", size=10)

register = Label(text="Sign Up", font=Font_style, fg="Green").grid(row=0, column=0, columnspan=2, pady=5)
name = Label(text="Name:", font=Font_style_2, fg="Blue").grid(row=1, column=0, pady=5)
txt_name = Entry(font=Font_style_2, width=15, fg="Green").grid(row=1, column=1, pady=5)
user_name = Label(text="User Name:", font=Font_style_2, fg="Blue").grid(row=2, column=0, pady=5)
txt_username = Entry(font=Font_style_2, width=15, fg="Purple").grid(row=2, column=1, pady=5)
password = Label(text="Password:", font=Font_style_2, fg="Blue").grid(row=3, column=0, pady=5)
txt_pass = Entry(font=Font_style_2, width=15, fg="Brown").grid(row=3, column=1, pady=5)
contact = Label(text="Contact:", font=Font_style_2, fg="Blue").grid(row=4, column=0, pady=5)
txt_contact = Entry(font=Font_style_2, width=15, fg="Green").grid(row=4, column=1, pady=5)
gender = Label(text="Gender:", font=Font_style_2, fg="Blue").grid(row=5, column=0, pady=5)
txt_gen = OptionMenu(window, sub, "male", "female").grid(row=5, column=1, pady=5)
select = Label(text="Select Position:", font=Font_style_2, fg="Blue").grid(row=6, column=0, pady=5)
txt_Select = OptionMenu(window, opt, *option).grid(row=6, column=1, pady=5)
terms = Checkbutton(text="Agree Terms and Policies", variable=term, fg="Purple").grid(row=7, column=1, pady=5)
bt_sign = Button(command=valid, text="Sign In", font=Font_style_2, fg="Green").grid(row=10, column=0, pady=5)
bt_cancel = Button(command=CloseWindow, text="Cancel", font=Font_style_2, fg="Red").grid(row=10, column=1, pady=5)

window.mainloop()