import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Checkbutton")

# check_button = ttk.Checkbutton(root, text="Check me!")
# check_button.pack()
# check_button["state"]="disabled"

selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())

# variable=selected_option, variable whoese value depends on check status of the button
# onvalue specifies the value when it's on, offvalue otherwise
check = ttk.Checkbutton(
    root,
    text="Check example",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
).pack()

root.mainloop()