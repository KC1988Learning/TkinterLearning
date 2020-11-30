import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Separator")

ttk.Label(root, text="Rectangle 1", padding=(20,10,20,10)).pack()
ttk.Separator(root).pack(fill="x")
ttk.Label(root, text="Rectangle 2", padding=(20,10,20,10)).pack()


root.mainloop()
