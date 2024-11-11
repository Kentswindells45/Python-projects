import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3

# creating a data base and connecting to it we use a variable to create the connection of the database does con_db
con_db = sqlite3.connect("StuData.db")

# create a cursor go and retrieve data from the database by using a variable plus the connection . cursor
c = con_db.cursor()

# creating a table
# comment sqlite3 table with''''''

c.execute("""CREATE TABLE IF NOT EXISTS students(
    student_Name text,
    user_name text primary key,
    gender text,
    course text,
    contact text
)""")

# save changes
con_db.commit()

# close connection of the database after use
con_db.close()


# Data insertion to the Database

def insertData():
    if nam.get() == "" or txt_u_name.get() == "" or genVar.get() == "Select Gender" or \
            txt_course.get() == "" or txt_contact.get() == "":
        messagebox.showerror("Fill", "Fill all blank space")
    else:
        con__db = sqlite3.connect("StuData.db")
        c__c = con__db.cursor()
        # inserting data
        c__c.execute("INSERT INTO students VALUES (:stName,:uname,:gen,:stcourse,:stcontact)",
                     {
                         'stName': nam.get(),
                         'uname': txt_u_name.get(),
                         'gen': genVar.get(),
                         'stcourse': txt_course.get(),
                         'stcontact': txt_contact.get()

                     }
                     )
        messagebox.showinfo("Successfully", "Data Inserted")
        nam.delete(0, END)
        txt_u_name.delete(0, END)
        genVar.set("Select Gender")
        txt_course.delete(0, END)
        txt_contact.delete(0, END)

        con__db.commit()
        con__db.close()


# Create Edit Function to update a record
global update


def update():
    con__db = sqlite3.connect("StuData.db")
    c__c = con__db.cursor()
    record_id = EditData.get()
    c__c.execute("""UPDATE students set
                student_Name=:student,
                user_name =:user,
                gender=:gender,
                course =:course,
                contact=:contact
            
                WHERE oid =:oid """,
                 {
                     'student': nam_m.get(),
                     'user_name': txt_u__name.get(),
                     'gender': txt__gender.get(),
                     'course': txt__course.get(),
                     'contact': txt_cont.get(),
                     'oid': record_id

                 })
    con__db.commit()
    con__db.close()


# creating Global variables


def EditData():
    editor = Tk()
    editor.title(" Edit")
    # editor.iconbitmap("E:/UI")
    editor.resizable("true", "true")
    editor.geometry("300x340")
    editor.eval("tk::PlaceWindow . center")
    con__db = sqlite3.connect("StuData.db")
    c_c = con__db.cursor()
    font_style__2 = tkFont.Font(family="Helvetica", size=10)
    font__style = tkFont.Font(family="Corbel", size=18)

    t_title = Label(editor, text="Edit Data", font=font__style, fg="Blue")
    f__name = Label(editor, text="Student Name", font=font_style__2, fg="Brown")
    nam_m = Entry(editor, font=font__style, width=15, bd=5)
    u__name = Label(editor, text="User Name", font=font_style__2, fg="Brown")
    txt_u__name = Entry(editor, font=font__style, width=15, bd=5)
    pas = Label(editor, text="Password", font=font_style__2, fg="Brown")
    txt_pas = Entry(editor, font=font__style, width=15, bd=5)
    g_gender = Label(editor, text="Gender", font=font_style__2, fg="Brown")
    txt__gender = Entry(editor, font=font__style, width=15, bd=5)
    course_c = Label(editor, text="Course", font=font_style__2, fg="Brown")
    txt__course = Entry(editor, font=font__style, width=15, bd=5)
    cont = Label(editor, text="Contact", font=font_style__2, fg="Brown")
    txt_cont = Entry(editor, font=font__style, width=15, bd=5)
    update = Button(editor, text="Update", font=font_style__2, fg="Green", bd=5, command=EditData)
    # bt_cancel = Button(editor, text="View", font=font_style_2, fg="Red", bd=5)

    t_title.grid(row=0, column=0, columnspan=2, pady=5)
    f__name.grid(row=1, column=0, pady=5)
    nam_m.grid(row=1, column=1, pady=5)
    u__name.grid(row=2, column=0, pady=5)
    txt_u__name.grid(row=2, column=1, pady=5)
    g_gender.grid(row=3, column=0, pady=5)
    txt__gender.grid(row=3, column=1, pady=5)
    course_c.grid(row=4, column=0, pady=5)
    txt__course.grid(row=4, column=1, pady=5)
    cont.grid(row=5, column=0, pady=5)
    txt_cont.grid(row=5, column=1, pady=5)
    update.grid(row=6, column=0, pady=5)
    # bt_cancel.grid(row=6, column=1, pady=5)

    c_c.execute("SELECT * from students WHERE oid =" + del_id.get())
    records = c_c.fetchall()
    for record in records:
        nam_m.insert(0, record[0])
        txt_u__name.insert(0, record[1])
        txt__gender.insert(0, record[2])
        txt__course.insert(0, record[3])
        txt_cont.insert(0, record[4])

    con__db.commit()
    con__db.close()


# Function to delete from a record

def delData():
    res = messagebox.askquestion("Confirm Delete", "Are you sure you want to delete?")
    if res == "yes":
        con___db = sqlite3.connect("StuData.db")
        c___c = con___db.cursor()
        c___c.execute("DELETE FROM students WHERE oid = " + del_id.get())
        del_id.delete(0, END)
        con___db.commit()
        con___db.close()
        data.destroy()
        getData()


#  Fetching information from Database
def getData():
    global del_id
    global data
    text = StringVar()
    const = StringVar()
    cours = StringVar()
    genn = StringVar()
    un = StringVar()
    num = StringVar()
    con__db = sqlite3.connect("StuData.db")
    c_c = con__db.cursor()

    # code to select data
    # oid means object id
    data = Toplevel()
    data.title("STUDENT DATA")
    # data.iconbitmap("E:/UI")
    data.resizable("false", "false")
    data.geometry("390x300")
    c_c.execute("SELECT *, oid from students")
    records = c_c.fetchall()
    #    print_records = ''
    i = 3
    for stData in records:
        for column in range(len(stData)):
            unknown = StringVar()
            sData = Entry(data, state=DISABLED, textvariable=unknown, width=10, fg="Blue")
            unknown.set(stData[column])
            sData.grid(row=i, column=column)
            sData.insert(END, stData[column])
        i += 1

    # TO SHOW ALL DATA ONCE
    # print_records += str(stData)+ "\n"
    # To display One record from the Data at index 0,1,2 .......
    # print_records += str(stData[0]) + " " + str(stData[1]) + " " + str(stData[4]) + "\n"
    student_Name = Entry(data, state=DISABLED, textvariable=num, width=10, fg="Red")
    student_Name.insert(END, "NAME")
    student_Name.grid(row=2, column=0)
    user_name = Entry(data, state=DISABLED, textvariable=num, width=10, fg="Red")
    num.set("Name")
    un.set("User Name")
    user_name.insert(END, "User Name")
    user_name.grid(row=2, column=1)
    gendd = Entry(data, state=DISABLED, textvariable=genn, width=10, fg="Red")
    genn.set("Gender")
    gendd.insert(END, "Gender")
    gendd.grid(row=2, column=2)
    cos = Entry(data, state=DISABLED, textvariable=cours, width=10, fg="Red")
    cours.set("Course")
    cos.insert(END, "Course")
    cos.grid(row=2, column=3)
    cont = Entry(data, state=DISABLED, textvariable=const, width=10, fg="Red")
    const.set("Contact")
    cont.insert(END, "Contact")
    cont.grid(row=2, column=4)
    idd = Entry(data, state=DISABLED, textvariable=text, width=10, fg="Red")
    text.set("ID")
    idd.insert(END, "ID")
    idd.grid(row=2, column=5)
    st = Label(data, text="REGISTRATION INFO", fg="Green")
    st.grid(row=0, column=0, columnspan=8)
    del_id = Entry(data, width=10, fg="Orange")
    del_id.grid(row=1, column=0)

    btdel = Button(data, text="Delete", bg="Pink", bd=5, command=delData)
    btdel.grid(row=1, column=1)
    btedit = Button(data, text="Edit", bg="Pink", bd=5, command=EditData)
    btedit.grid(row=1, column=2)
    # res_label = Label(data, text=print_records)
    # res_label.grid(row=1, column=0)
    #    print(records)

    con__db.commit()
    con__db.close()


# Root Window Skeleton

system = tkinter.Tk()
system.title("STUDENT MANAGEMENT SYSTEM")
# system.iconbitmap("E:/UI")
system.resizable("true", "true")
system.geometry("300x340")
system.eval("tk::PlaceWindow . center")

# def CloseWindow():
#    response = messagebox.askquestion("Confirm", "Do you want to close window")
#    if response == "yes":
#        system.destroy()


genVar = StringVar()
genVar.set("Select Gender")

font_style_2 = tkFont.Font(family="Helvetica", size=10)
font_style = tkFont.Font(family="Corbel", size=18)

title = Label(text="STUDENT'S ATTENDANCE ", font=font_style, fg="Blue")
f_name = Label(text="Student Name", font=font_style_2, fg="Brown")
nam = Entry(font=font_style, width=15, bd=5)
u_name = Label(text="User Name", font=font_style_2, fg="Brown")
txt_u_name = Entry(font=font_style, width=15, bd=5)
pas = Label(text="Password", font=font_style_2, fg="Brown")
txt_pas = Entry(font=font_style, width=15, bd=5)
gender = Label(text="Gender", font=font_style_2, fg="Brown")
txt_gender = OptionMenu(system, genVar, "Male", "Female")
course = Label(text="Course", font=font_style_2, fg="Brown")
txt_course = Entry(font=font_style, width=15, bd=5)
contact = Label(text="Contact", font=font_style_2, fg="Brown")
txt_contact = Entry(font=font_style, width=15, bd=5)
bt_sign = Button(command=insertData, text="Sign Up", font=font_style_2, fg="Green", bd=5)
bt_cancel = Button(command=getData, text="View", font=font_style_2, fg="Red", bd=5)

title.grid(row=0, column=0, columnspan=2, pady=5)
f_name.grid(row=1, column=0, pady=5)
nam.grid(row=1, column=1, pady=5)
u_name.grid(row=2, column=0, pady=5)
txt_u_name.grid(row=2, column=1, pady=5)
gender.grid(row=3, column=0, pady=5)
txt_gender.grid(row=3, column=1, pady=5)
course.grid(row=4, column=0, pady=5)
txt_course.grid(row=4, column=1, pady=5)
contact.grid(row=5, column=0, pady=5)
txt_contact.grid(row=5, column=1, pady=5)
bt_sign.grid(row=6, column=0, pady=5)
bt_cancel.grid(row=6, column=1, pady=5)

system.mainloop()

# to make the entry un edited use the (state ="readonly")
