import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# fix size of the main window
root.geometry("600x400")

# create first label
rect1 = tk.Label(root, text="Rectangle 1", background="green", foreground="white")
rect1.pack(ipadx=10, ipady=10, side="left", fill="both", expand=True)


# create second label
rect2 = tk.Label(root, text="Rectangle 2", background="red", foreground="white")
rect2.pack(ipadx=10, ipady=10, side="top", fill="both", expand=True)

# create third label
rect3 = tk.Label(root, text="Rectangle 3", background="black", foreground="white")
rect3.pack(ipadx=10, ipady=10, side="left", fill="both", expand=True)

root.mainloop()