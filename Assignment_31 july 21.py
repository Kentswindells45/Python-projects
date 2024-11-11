import tkinter
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox

main = tkinter.Tk()
main.title("Form")
main.resizable("true", "true")
main.iconbitmap("E:/UI")
main.geometry("420x390")
main.eval("tk::PlaceWindow . center")


def NewWindow():
    if txt_f_name == "" or txt_s_name == "" or txt_pass == "":
        if gender == 1 or gender == 0:
            if Checkbutton == 1:
                new = Toplevel()
                new.resizable("true", "true")
                new.iconbitmap("E:/UI")
                new.geometry("420x290")
                fn = txt_f_name.get()
                ln = txt_s_name.get()
                pas = txt_pass.get()
                f = Label(new, text="First Name: " + fn, fg="Black", font=font_style).place(x=10, y=20)
                s = Label(new, text="Last Name: " + ln, fg="Black", font=font_style).place(x=10, y=60)
                pw = Label(new, text="Password: " + pas, fg="Black", font=font_style).place(x=10, y=100)
                bt_cancel = Button(new, command=new.destroy, text="Close This Window", bg="Blue", fg="White")
                bt_cancel.place(x=100, y=150)
                return f, s, pw
            else:

                msg = messagebox.showwarning("Warning", "Fill the Blank space")
        else:
            msg = messagebox.showwarning("Warning", "Fill the Blank space")
    else:
        msg = messagebox.showwarning("Warning", "Fill the Blank space")


font_style = tkFont.Font(family="Helvetica", size=15)
font_style2 = tkFont.Font(family="Italic", size=15)


def CloseWindow():
    response = messagebox.askquestion("Confirm", "Do you want to close this window?")
    if response == "yes":
        main.destroy()


gender = StringVar()
terms = IntVar()

register = Label(text="Sign In", font=font_style)
first_name = Label(text="First Name:", font=font_style2, width=15)
txt_f_name = Entry(font=font_style, width=15, fg="Blue")
second_name = Label(text="Second Name:", font=font_style2, width=15)
txt_s_name = Entry(font=font_style, width=15, fg="Blue")
password = Label(text="Password:", font=font_style2, width=15)
txt_pass = Entry(font=font_style, width=15, fg="Blue")
bt_sign = Button(command=NewWindow, text="Sign In", font=font_style2, fg="White", bg="Blue")
bt_close = Button(command=CloseWindow, text="Close", font=font_style2, fg="White", bg="Blue")
rad_male = Radiobutton(text="Male", value="Male",variable=gender)
rad_female = Radiobutton(text="Female", value="Female",variable=gender)
terms = Checkbutton(text="Agree Terms And Policy", variable=gender)

register.grid(row=0, column=0, columnspan=2, pady=5)
first_name.grid(row=1, column=0, pady=5)
txt_f_name.grid(row=1, column=1, pady=5)
second_name.grid(row=2, column=0, pady=5)
txt_s_name.grid(row=2, column=1, pady=5)
password.grid(row=3, column=0, pady=5)
txt_pass.grid(row=3, column=1, pady=5)
rad_male.grid(row=4, column=0, pady=5)
rad_female.grid(row=4, column=1, pady=5)
terms.grid(row=5, column=0, pady=5)
bt_sign.grid(row=7, column=0, pady=5)
bt_close.grid(row=7, column=1, pady=5)

main.mainloop()
