import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Listbox")

initial_value = tk.IntVar(value=20)

# you can also use ttk.Spinbox for Python 3.7 above
# to go back to initial value when maximum is hit, set wrap as True
# remember that from_ has a final underscore to avoid conflict with
# Python key word from
spin_box = tk.Spinbox(
    root,
    from_ = 0,
    to = 30,
    textvariable = initial_value,
    wrap=False
)
spin_box.pack(padx=(20,20), pady=(10,10))

ttk.Separator(root).pack(fill="x")

another_value = tk.IntVar(value=0)
spin_box_discrete = ttk.Spinbox(
    root,
    values=(0,5,10,15,20),
    textvariable = another_value,
    wrap=True,
)
spin_box_discrete.pack(padx=(20,20), pady=(10,10))

root.mainloop()