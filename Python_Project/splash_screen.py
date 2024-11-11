from tkinter import *

root = Tk()
root.title("Splash Screen")
root.resizable("false", "false")

main_root = Label(root, text="Splash Screen", font=("Helvetica", 18))
main_root.pack(pady=20)


def main_window():
    root.destroy()
    main_win = Tk()
    main_win.title("main screen")
    main_win.geometry("360x320")

    mmk = Label(main_win, text="Main Screen", font=("Helvetica", 18))
    mmk.pack(pady=20)


root.after(3000, main_window)

root.mainloop()