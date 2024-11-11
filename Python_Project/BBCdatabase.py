import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3

KENT_INC__CORP_ = "Kent Inc. Corp "

db = sqlite3.connect("BCdata.db")
c = db.cursor()

# creating database tables
c.execute("""CREATE TABLE IF NOT EXISTS church(
    Member_name text,
    Residence text,
    Gender text,
    Contact text primary key,
    Corresponding_Position text
)""")
db.commit()
db.close()

#data insertion 
def DataInsertion():
    if txt_name.get() == "" or txt_res.get() == "" or genVar.get() == "Select Gender" \
            or txt_contact.get() == "" or post.get() == "Select Corresponding Position":
        messagebox.showerror("Error", "fill all blank Spaces")
    else:
        db = sqlite3.connect("BCdata.db")
        c = db.cursor()
        c.execute("INSERT INTO church VALUES (:stName,:uname,:gen,:stcourse,:stcontact)",
                  {
                      "stName": txt_name.get(),
                      "uname": txt_res.get(),
                      "gen": genVar.get(),
                      "stcourse": txt_contact.get(),
                      "stcontact": post.get()

                  }
                  )
        messagebox.showinfo("Successfully", "Data Insertion Successful!!")
        txt_name.delete(0, END)
        txt_res.delete(0, END)
        genVar.set("Select Gender")
        txt_contact.delete(0, END)
        post.set("Select Corresponding Position")
        db.commit()
        db.close()


log = tkinter.Tk()
log.title("BBC PORTAL")
log.resizable("false", "false")
#log.iconbitmap("E:/UI")
log.geometry("350x390")
log.eval("tk::PlaceWindow . center")
#log.('blue')

position = [
    "Youth President",
    "Vice President",
    "Youth Organizer",
    "Youth Secretary",
    "Prayer Secretary",
    "Finance Secretary",
    "Usher",
    "Member"
]

post = StringVar()
post.set(position[0])
post.set("Select Corresponding Position")

genVar = StringVar()
genVar.set("Select Gender")

term = IntVar()


def delete():
    prompt = messagebox.askquestion("Delete", "Are you sure you want to delete?")
    if prompt == "yes":
        db = sqlite3.connect("BCdata.db")
        c = db.cursor()
        c.execute("DELETE FROM church WHERE oid =" + del_id.get())
        del_id.delete(0, END)
        db.commit()
        db.close()
        root.destroy()
        getData()


def Edit():
    edit = Tk()
    edit.title(" Edit")
    #edit.iconbitmap("E:/UI")
    edit.resizable ("true", "true")
    edit.geometry("300x340")
    edit.eval("tk::PlaceWindow . center")
    con__db = sqlite3.connect("BCdata.db")
    c_c = con__db.cursor()
    font_Style = tkFont.Font(family="Helvetica", size=15)
    font_Style2 = tkFont.Font(family="Corbel", size=10)

    title = Label(edit, text="Edit Information", font=font_Style, fg="Blue")
    name = Label(edit, text="Name:", font=font_Style, fg="Brown")
    txt_name = Entry(edit, font=font_Style2, width=20, fg="Green", bd=5)
    res = Label(edit, text="Residence:", font=font_Style, fg="Brown")
    txt_res = Entry(edit, font=font_Style2, width=20, fg="Green", bd=5)
    Ge_nn = Label(edit, text="Gender:", font=font_Style, fg="Brown")
    txt_gen = Entry(edit, font=font_Style2, width=20, fg="Green", bd=5)
    contact = Label(edit, text="Contact:", font=font_Style, fg="Brown", bd=5)
    txt_contact = Entry(edit, font=font_Style2, width=20, fg="Green", bd=5)
    pos = Label(edit, text="Position:", font=font_Style, fg="Brown")
    posit = Entry(edit, font=font_Style2, width=20, fg="Green", bd=5)
    bt_submit = Button(edit, font=font_Style2, text="Update", fg="Green", bd=5)

    title.grid(row=0, column=0, columnspan=2, pady=5)
    name.grid(row=1, column=0, pady=5)
    txt_name.grid(row=1, column=1, pady=5)
    res.grid(row=2, column=0, pady=5)
    txt_res.grid(row=2, column=1, pady=5)
    Ge_nn.grid(row=3, column=0, pady=5)
    txt_gen.grid(row=3, column=1, pady=5)
    contact.grid(row=4, column=0, pady=5)
    txt_contact.grid(row=4, column=1, pady=5)
    pos.grid(row=5, column=0, pady=5)
    posit.grid(row=5, column=1, pady=5)
    terms.grid(row=6, column=1, pady=5)
    bt_submit.grid(row=7, column=0, pady=5)

    c_c.execute("SELECT * from church WHERE oid =" + del_id.get())
    infos = c_c.fetchall()
    for info in infos:
        txt_name.insert(0, info[0])
        txt_res.insert(0, info[1])
        txt_gen.insert(0, info[2])
        txt_contact.insert(0, info[3])
        posit.insert(0, info[4])
    con__db.commit()
    con__db.close()


def getData():
    global del_id
    global root
    first = StringVar()
    second = StringVar()
    third = StringVar()
    fourth = StringVar()
    fifth = StringVar()
    sixth = StringVar()

    root = Toplevel()
    root.title("CHURCH DATA")
    #root.iconbitmap("E:/UI")
    root.resizable("true", "true")
    root.geometry("490x340")
    db = sqlite3.connect("BCdata.db")
    c = db.cursor()
    c.execute("SELECT*, oid from church")
    retrieve = c.fetchall()
    i = 3
    for churchData in retrieve:
        for column in range(len(churchData)):
            disable = StringVar()
            cData = Entry(root, state=DISABLED, textvariable=disable, width=13, fg="Blue")
            disable.set(churchData[column])
            cData.grid(row=i, column=column)
            cData.insert(END, churchData[column])
        i += 1
    txt_name = Entry(root, state=DISABLED, textvariable=first, width=13, fg="Violet")
    first.set("Name")
    txt_name.insert(END, "NAME")
    txt_name.grid(row=2, column=0)
    txt_res = Entry(root, state=DISABLED, textvariable=second, width=13, fg="Violet")
    second.set("Residence")
    txt_res.insert(END, "Residence")
    txt_res.grid(row=2, column=1)
    txt_gen = Entry(root, state=DISABLED, textvariable=third, width=13, fg="Violet")
    third.set("Gender")
    txt_gen.insert(END, "Gender")
    txt_gen.grid(row=2, column=2)
    txt_contact = Entry(root, state=DISABLED, textvariable=fourth, width=13, fg="Violet")
    fourth.set("Contact")
    txt_contact.insert(END, "Contact")
    txt_contact.grid(row=2, column=3)
    posit = Entry(root, state=DISABLED, textvariable=fifth, width=13, fg="Violet")
    fifth.set("Position")
    posit.insert(END, "Position")
    posit.grid(row=2, column=4)
    idd = Entry(root, state=DISABLED, textvariable=sixth, width=13, fg="Red")
    sixth.set("ID")
    idd.insert(END, "ID")
    idd.grid(row=2, column=5)
    st = Label(root, text="Members INFO", fg="Green")
    st.grid(row=0, column=0, columnspan=8)
    del_id = Entry(root, width=10, fg="Orange", bd=5)
    del_id.grid(row=1, column=0)

    btdel = Button(root, text="Delete", bg="Pink", bd=5, command=delete)
    btdel.grid(row=1, column=1)
    btedit = Button(root, text="Edit", bg="Pink", bd=5, command=Edit)
    btedit.grid(row=1, column=2)

    db.commit()
    db.close()


def CloseWindow():
    response = messagebox.askquestion("Prompt", "Do you Want to  Close Window?")
    if response == "yes":
        log.destroy()


font_Style = tkFont.Font(family="Helvetica", size=15)
font_Style2 = tkFont.Font(family="Corbel", size=10)
font_style3 = tkFont.Font(family="Corbel", size=8)

title = Label(text="BBC YOUTH PORTAL", font=font_Style, fg="Blue")
name = Label(text="Name:", font=font_Style, fg="Brown")
txt_name = Entry(font=font_Style2, width=20, fg="Green", bd=5)
res = Label(text="Residence:", font=font_Style, fg="Brown")
txt_res = Entry(font=font_Style2, width=20, fg="Green", bd=5)
Ge_nn = Label(text="Gender:", font=font_Style, fg="Brown")
txt_gen = OptionMenu(log, genVar, "Male", "Female")
contact = Label(text="Contact:", font=font_Style, fg="Brown", bd=5)
txt_contact = Entry(font=font_Style2, width=20, fg="Green", bd=5)
pos = Label(text="Position:", font=font_Style, fg="Brown")
posit = OptionMenu(log, post, *position)
terms = Checkbutton(text="Agree to Submit Data", font=font_Style2, variable=term,
                    fg="Purple")
bt_submit = Button(command=DataInsertion, text="Submit", font=font_Style2, fg="Orange", bd=5, bg="Green")
bt_cancel = Button(command=CloseWindow, text="Cancel", font=font_Style2, fg="Red", bd=5, bg="Pink")
sign = Label(text="KENT_INC__CORP_(c)2021", font=font_style3, fg="Blue")
bt_view = Button(command=getData, text="View", font=font_Style2, bd=5, fg="Brown", bg="White")

title.grid(row=0, column=0, columnspan=2, pady=5)
name.grid(row=1, column=0, pady=5)
txt_name.grid(row=1, column=1, pady=5)
res.grid(row=2, column=0, pady=5)
txt_res.grid(row=2, column=1, pady=5)
Ge_nn.grid(row=3, column=0, pady=5)
txt_gen.grid(row=3, column=1, pady=5)
contact.grid(row=4, column=0, pady=5)
txt_contact.grid(row=4, column=1, pady=5)
pos.grid(row=5, column=0, pady=5)
posit.grid(row=5, column=1, pady=5)
terms.grid(row=6, column=1, pady=5)
bt_submit.grid(row=7, column=0, pady=5)
bt_view.grid(row=7, column=1, pady=5)
bt_cancel.grid(row=8, column=0, pady=5)
sign.grid(row=10, column=0, pady=5)

log.mainloop()
