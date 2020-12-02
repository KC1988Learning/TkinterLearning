import tkinter as tk
from tkinter import ttk
from tutorial.window import set_dpi_awareness

set_dpi_awareness()


# inherit from tk.Tk class
# helloWorld is a copy of tk.Tk (main window class)

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__() # call an instance of the super class and initialize it

        # set the title of the HelloWorld instance, inherited from tk.Tk
        self.title("Hello, World!")

        # create a label
        ttk.Label(self, text="Hello, World!").pack()


root = HelloWorld()
root.mainloop()