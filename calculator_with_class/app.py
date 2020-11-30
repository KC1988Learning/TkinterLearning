import tkinter as tk
from tkinter import ttk
from tutorial.window import set_dpi_awareness

set_dpi_awareness()

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        

root = HelloWorld()
root.mainloop()