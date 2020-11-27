import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

def greet():
    # add strip() to remove whitespace in string
    print(f"Hello {user_name.get().strip() or 'World'}! How are you?")

set_dpi_awareness()

root = tk.Tk()
root.title("Greeting App")

# configure row and column property of the root window
# weight = 0, column/row takes up size of the content
# weight is relative, if one is 0 another is 1, 1 means taking up all space
# if one is 2 another 1, means the first one occupies twice as much space

root.columnconfigure(index=0, weight=1)

user_name = tk.StringVar()
user_age = tk.IntVar()

# padding = (left, top, right, bottom)
entry_frame = ttk.Frame(root, padding=(20,10, 20, 0))

# grid will place the element on the first available row in the first column
# sticky = EW: makes the column 'sticks' to the edge of the root window
entry_frame.grid(row=0, column=0, sticky='EW')

# column 0 and 1 in entry_frame as wide as needed by the content
entry_frame.columnconfigure(index=0, weight=0)
entry_frame.columnconfigure(index=1, weight=0)

user_label = ttk.Label(entry_frame, text="Name: ")
# weight=0: takes as space as needed by the content
user_label.grid(row=0, column=0, sticky='EW')

user_entry = ttk.Entry(entry_frame, width=15, textvariable=user_name)
user_entry.grid(row=0, column=1, sticky='EW')
user_entry.focus()

# padding = (horizontal, vertical)
btn_frame = ttk.Frame(root, padding=(20, 10))
# sticky='EW' makes the row sticks to the root window
btn_frame.grid(row=1, column=0, sticky='EW')

# make the first column takes up one portion of the width of btn_frame
btn_frame.columnconfigure(index=0, weight=1)
greet_btn = ttk.Button(btn_frame, text="Greet", command=greet)
# sticky = 'EW' makes the buttom stick to the boundary of the first column
greet_btn.grid(row=0, column=0, sticky='EW')

btn_frame.columnconfigure(index=1, weight=1)
quit_btn = ttk.Button(btn_frame, text="Quit", command=root.destroy)
quit_btn.grid(row=0, column=1, sticky='EW')

root.mainloop()
