import tkinter as tk
from tkinter.filedialog import askopenfilename

location = ""
root = tk.Tk()
root.withdraw()
location = askopenfilename(defaultextension=".db", title="Choose your Database",
                           filetypes=[("Database File", ".db"), ("All files", "*")])
start = tk.Tk()
tk.Label(start, text="What is the name of your table?").pack()
box = tk.Entry(start, exportselection=0, state=tk.DISABLED)
box.pack()
start.focus_set()
box.focus_set()
start.focus_force()
button = tk.Button(start, text="OK", bd=5, command=lambda e: None)
button.pack()
box.config(state=tk.NORMAL)
start.mainloop()
