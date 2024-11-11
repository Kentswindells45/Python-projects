from tkinter import *


def gui():
    root = Tk()
    root.geometry("200x200+50+100")
    text = StringVar()
    mk = StringVar()
    entry = Entry(root, state=DISABLED, textvariable=text, width=12)
    text.set("ID")
    entry.pack(padx=10, pady=10)
    mmk = Entry(root, state=DISABLED, textvariable=mk, width=12)
    mk.set("kent")
    mmk.pack()

    root.mainloop()


gui()
