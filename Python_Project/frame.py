import tkinter as tk


class HelloWorld(object):
    pass


def self(args):
    pass


class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)
        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack(padx=200, pady=200)


if __name__ == "__main__":
    root = tk.Tk()
    main = HelloWorld(root)
    main.pack(fill="both", expand=True)

    root.mainloop()
