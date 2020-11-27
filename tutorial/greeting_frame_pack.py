import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello {user_name.get() or 'World'}! How are you?")

root = tk.Tk()
root.title("Greeting App")

user_name = tk.StringVar()
user_age = tk.IntVar()

# padding = (left, top, right, bottom)
entry_frame = ttk.Frame(root, padding=(20,10, 20, 0))
entry_frame.pack(side="top", fill="x")

user_label = ttk.Label(entry_frame, text="Name: ")
user_label.pack(side="left", expand=False)

user_entry = ttk.Entry(entry_frame, width=15, textvariable=user_name)
user_entry.pack(side="left", expand=False)
user_entry.focus()

# padding = (horizontal, vertical)
btn_frame = ttk.Frame(root, padding=(20, 100))
btn_frame.pack(side="top", fill="x")

greet_btn = ttk.Button(btn_frame, text="Greet", command=greet)
greet_btn.pack(side="left", expand=True, fill="x")

quit_btn = ttk.Button(btn_frame, text="Quit", command=root.destroy)
quit_btn.pack(side="left", expand=True, fill="x")

root.mainloop()
