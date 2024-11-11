import tkinter
from tkinter import *
import tkinter.font as mk_font
from tkinter import messagebox

college = Tk()
college.title("College Application Forms")
college.resizable("true", "true")
college.iconbitmap("E:/UI")
college.geometry("350x550")
college.eval("tk::PlaceWindow . center")

font_style = mk_font.Font(family="Helvetica", size=12)
font_style2 = mk_font.Font(family="Corbel", size=12)


def close_win():
    prompt = messagebox.askquestion("Prompt", "Do you want to close form?")
    if prompt == "yes":
        college.destroy()


lab = Label(text="College Application Form", font=font_style, fg="Blue")
lab2 = Label(text="Please fill in the college application \n"
                  "form below if you want to attend our institution.\n Thank You", font=font_style2, fg="Green")
nam = Label(text="Title:", font=font_style, fg="Brown")
txt_nam = Entry(font=font_style2, width=12)
title = Label(text="Name:", font=font_style, fg="Brown")
txt_first = Entry(font=font_style2, width=30)
Dob = Label(text="Date of Birth:", font=font_style, fg="Brown")
txt_Dob = Entry(font=font_style2, width=20)
phone = Label(text="Phone:", font=font_style, fg="Brown")
txt_phone = Entry(font=font_style2, width=30)
radio_male = Radiobutton(text="Male", value="Male")
radio_female = Radiobutton(text="Female", value="Female")
agree_term = Checkbutton(text="Agree Terms and Policy", fg="Blue")
btsign = Button(text="Submit", font=font_style2, fg="Green")
btcancle = Button(command=close_win, text="Close", font=font_style2, fg="Red")

lab.grid(row=0, column=0, columnspan=2, pady=5)
lab2.grid(row=1, column=0, pady=5)
nam.grid(row=2, column=0, pady=5)
txt_nam.grid(row=3, column=0, pady=5)
title.grid(row=4, column=0, pady=5)
txt_first.grid(row=5, column=0, pady=5)
Dob.grid(row=6, column=0, pady=5)
txt_Dob.grid(row=7, column=0, pady=5)
phone.grid(row=8, column=0, pady=5)
txt_phone.grid(row=9, column=0, pady=5)
radio_male.place(x=100, y=380)
radio_female.place(x=190, y=380)
agree_term.place(x=95, y=410)
btsign.place(x=100, y=470)
btcancle.place(x=200, y=470)

college.mainloop()
