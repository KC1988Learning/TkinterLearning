import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

set_dpi_awareness()

def print_weekday():
    print(selected_weekday.get().strip())

def handle_selection(event):
    print("Today is ", selected_weekday.get() + ".")
    print("But we are going to change it to Friday.")
    selected_weekday.set("Friday")
    # print current value, otherwise .get() also works
    print(weekday.current())

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Combo Box")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("", "Monday", "Tuesday", "Wednesday","Thursday", "Friday")
# set state to readonly so that user can only select and cannot key in anything else
weekday["state"] = "readonly" # "normal"
weekday.pack()

# bind the element to an event listener, and execute something when the event occurs
weekday.bind("<<ComboboxSelected>>", handle_selection)


# btn = ttk.Button(root, text="Click me", command=print_weekday).pack()

root.mainloop()

print(selected_weekday.get(), " was selected.")