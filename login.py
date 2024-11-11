import tkinter
from tkinter import *
# to import tkinter font you need to call it and name it with a variable
import tkinter.font as tkFont
from tkinter import messagebox

display = tkinter.Tk()
display.title("Welcome Screen")
display.iconbitmap("E:/UI")
display.resizable("false", "false")
display.geometry("300x340")
display.eval("tk::PlaceWindow . center")


def login():
    log = Toplevel()
    log.title("Login")
    log.iconbitmap("E:/UI")
    log.resizable("false", "false")
    log.geometry("210x200")
    lb_login = Label(log, text="SignIn").grid(row=0, column=0)
    lub_name_1 = Label(log, text="User Name", font=fontStyle_2).grid(row=1, column=0, pady=3)
    txt_user_name = Entry(log, font=fontStyle_2).grid(row=2, column=0, pady=3)
    lub_name = Label(log, text="Password", font=fontStyle_2).grid(row=3, column=0, pady=3)
    txt_user_pass = Entry(log, font=fontStyle_2).grid(row=4, column=0, pady=3)
    bt = Button(log, text="SignIn").grid(row=5, column=0, pady=3)
    return lb_login, lub_name_1, txt_user_name, lub_name, txt_user_pass, bt


fonStyle_3 = tkFont.Font()


# to bring a new window we use the method Top level(initialize by
# using command = new_window to your desire button....
def new_window():
    new = Toplevel()
    new.iconbitmap("E:/UI")
    new.resizable("false", "false")
    new.geometry("200x240")
    lbfname = Label(new, text="Student Portal ", font=fontStyle, fg="Blue").grid(row=0, column=0, columnspan=2)
    welcome = Label(new, text="Welcome", fg="Green").grid(row=1, column=0, columnspan=2)
    full_details = Label(new, text="FULL DETAILS", fg="Brown").grid(row=2, column=0, columnspan=2)
    firstName = Label(new, text="First Name :").grid(row=3, column=0)
    tfName = Label(new, text=txtF_name.get()).grid(row=3, column=1)
    second = Label(new, text="Last Name :").grid(row=4, column=0)
    fn = Label(new, text=txtl_name.get()).grid(row=4, column=1)
    user = Label(new, text="User Name :").grid(row=5, column=0)
    users = Label(new, text=txtU_name.get()).grid(row=5, column=1)
    pp = Label(new, text="Password :").grid(row=6, column=0)
    pas = Label(new, text=txtPass.get()).grid(row=6, column=1)
    genders = Label(new, text="Gender :").grid(row=7, column=0)
    mf = Label(new, text=gen.get()).grid(row=7, column=1)

    btclose = Button(new, command=new.destroy, text="LOG OUT").grid(row=8, column=0, columnspan=2)
    # btclose.pack()


def validate():
    # response = messagebox.askyesno("Update", "You are about to sign in")
    genval = str(gen.get())
    tval = int(term.get())
    if txtF_name.get() == "" or txtl_name.get() == "" or txtU_name == "" \
            or txtPass == "" or tval != 1 or genval != "Male" and genval != "Female":
        messagebox.showerror("Error", "Fill all black spaces")
    else:
        new_window()


def check():
    genval = Label(text=gen.get())
    genval.grid(row=8, column=0, pady=5)


def CloseWindow():
    login()
    response = messagebox.askquestion("Confirm", "Do you want to close window")
    if response == "yes":
        display.destroy()


# Using a variable to check the radio buttons
# IntVar is used for numbers
# StringVar is used for strings
gen = StringVar()
term = IntVar()

fontStyle = tkFont.Font(family="Helvetica", size=18)
fontStyle_2 = tkFont.Font(family="Italic", size=10)
register = Label(text="Sign In", font=fontStyle)
f_name = Label(text="First Name:", font=fontStyle_2)
txtF_name = Entry(font=fontStyle_2, width=15)
l_name = Label(text="Last Name:", font=fontStyle_2)
txtl_name = Entry(font=fontStyle_2, width=15)
Uname = Label(text="User Name:", font=fontStyle_2)
txtU_name = Entry(font=fontStyle_2, width=15)
Pass = Label(text="Password:", font=fontStyle_2)
txtPass = Entry(font=fontStyle_2, width=15)
btsign = Button(command=validate, text="SignIn", font=fontStyle_2)
btcancle = Button(command=CloseWindow, text="Close", font=fontStyle_2)
radmale = Radiobutton(text="Male", value="Male", variable=gen)
radfemale = Radiobutton(text="Female", value="Female", variable=gen)
terms = Checkbutton(text="Agree to our Terms", variable=term)

# you can use column span and row span to move to the center
# pady is used to leave out space on the y coordinate
# padx is used to leave out space on the x coordinate

register.grid(row=0, column=0, columnspan=2, pady=5)
f_name.grid(row=1, column=0, pady=5)
txtF_name.grid(row=1, column=1, pady=5)
l_name.grid(row=2, column=0, pady=5)
txtl_name.grid(row=2, column=1, pady=5)
Uname.grid(row=3, column=0, pady=5)
txtU_name.grid(row=3, column=1, pady=5)
Pass.grid(row=4, column=0, pady=5)
txtPass.grid(row=4, column=1, pady=5)
radmale.grid(row=5, column=0, pady=5)
radfemale.grid(row=5, column=1, pady=5)
terms.grid(row=6, column=0, columnspan=2, pady=5)
btsign.grid(row=7, column=0, pady=5)
btcancle.grid(row=7, column=1, pady=5)

display.mainloop()
