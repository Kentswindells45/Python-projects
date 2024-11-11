import tkinter
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("TreeView")
root.iconbitmap("E:/UI")
root.geometry("500x750")

# Add style
style = ttk.Style()
# pick a theme
style.theme_use("default")
# configure our treeview colors

style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white"
                )
# change selected color
style.map('Treeview',
          background=[('selected', 'blue')])
# create treeview_frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)
# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#create treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the Screen
my_tree.pack(pady=20)

#configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# define columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Format colummns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favorite Pizza", anchor=W, width=140)

# headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Add Data
data = [
    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"],
    ["Tim", 3, "Mushroom"],
    ["Smith", 4, "Ham"],
    ["BOb", 5, "Onion"],
    ["Smith", 6, "Ham"],
    ["BOb", 7, "Onion"],
    ["Smith", 8, "Ham"],
    ["Smith", 4, "Ham"],
    ["BOb", 5, "Onion"],
    ["Smith", 6, "Ham"],
    ["BOb", 7, "Onion"],
    ["Smith", 8, "Ham"],
    ["Smith", 4, "Ham"],
    ["BOb", 5, "Onion"],
    ["Smith", 6, "Ham"],
    ["BOb", 7, "Onion"],
    ["Smith", 8, "Ham"],
    ["Smith", 4, "Ham"],
    ["BOb", 5, "Onion"],
    ["Smith", 6, "Ham"],
    ["BOb", 7, "Onion"],
    ["Smith", 8, "Ham"],
    ["BOb", 9, "Onion"],

]
# create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="",
                       values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="",
                       values=(record[0], record[1], record[2]), tags=('oddrow',))
    count += 1


# my_tree.insert(parent='', index='end', iid=0, text="",
#              values=("John", 0, "Pepperoni"))
# my_tree.insert(parent='', index='end', iid=1, text="",
#              values=("John", 1, "Pepperoni"))
# my_tree.insert(parent='', index='end', iid=2, text="",
#              values=("John", 2, "Pepperoni"))
# my_tree.insert(parent='', index='end', iid=3, text="",
 #              values=("John", 3, "Pepperoni"))
# my_tree.insert(parent='', index='end', iid=4, text="",
#              values=("John", 4, "Pepperoni"))

# Add child
# my_tree.insert(parent='', index='end', iid=5, text="Child",
#               values=("Smith", 1.4, "Peppers"))
#my_tree.move('5','0', '0')


# Labels
add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

# Entry Boxes
name_box = Entry(add_frame, bd=4)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame, bd=4)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame, bd=4)
topping_box.grid(row=1, column=2)

# Add Record Function


def add_record():
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")
    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="",
                       values=(name_box.get(), id_box.get(), topping_box.get()), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="",
                       values=(name_box.get(), id_box.get(), topping_box.get()), tags=('oddrow',))
    count += 1
    # clear the box
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

# Remove all Records


def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
# Remove one


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
# Remove Many Selected


def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)
# Select Record


def select_record():
    # Clear Entry Boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    # Grab Record number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # temp_label.config(text=values[0])

    # output to entry boxes
    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


# Save updated Record
def update_record():
    # Grab Record number
    selected = my_tree.focus()
    # save new data
    my_tree.item(selected, text="", values=(
        name_box.get(), id_box.get(), topping_box.get()))

    # Clear Entry Boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


# Buttons
select_butom = Button(root, text="Select Record", command=select_record)
select_butom.pack(pady=20)

update_buttom = Button(root, text="Save Record", command=update_record)
update_buttom.pack(pady=10)

add_record = Button(root, text="Add Record", command=add_record)
add_record.pack(pady=10)

# Removr all
remove_all = Button(root, text="Remove All Records", command=remove_all)
remove_all.pack(pady=10)

# Remove One
remove_one = Button(root, text="Remove One Selected", command=remove_one)
remove_one.pack(pady=10)

# Remove Many Selected
remove_many = Button(root, text="Remove Many Selected", command=remove_many)
remove_many.pack(pady=10)

temp_label = Label(root, text="")
temp_label.pack(pady=20)
root.mainloop()
