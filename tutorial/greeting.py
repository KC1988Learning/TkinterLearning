import tkinter as tk
from tkinter import ttk

def greet():
    # insert content of user_name into the greeting string
    print(f"Hello {user_name.get() or 'World'}! How are you?")

root = tk.Tk() # instantiate main window

# create entry field label
name_lbl = ttk.Label(root, text="Name: ")
name_lbl.pack(side="left", padx=(0,10))

# create placeholder for user name
user_name = tk.StringVar()
# create entry field, width refers to the number of characters that
# can be accommodated in the entry field
# textvariable allows you to link the text content to a variable in the program
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
# make it as focus so that user can type directly when the app opens up
name_entry.focus()

# create greeting button
greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side="left", fill="x", expand=True)

# create quit button
quit_btn = ttk.Button(root, text="Quit", command=root.destroy)
quit_btn.pack(side="right", fill="x", expand=True)

root.mainloop() # run main window