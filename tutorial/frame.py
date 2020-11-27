import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# ttk.Label(root, text="Label top", background="red").pack(side="top", expand=True, fill="both")
# ttk.Label(root, text="Label top", background="green").pack(side="top", expand=True, fill="both")
# ttk.Label(root, text="Label left", background="blue").pack(side="left", expand=False, fill="both")

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

ttk.Label(main, text="Label top", background="red").pack(side="top", expand=True, fill="both")
ttk.Label(main, text="Label top", background="green").pack(side="top", expand=True, fill="both")

ttk.Label(root, text="Label left", background="blue").pack(side="left", expand=True, fill="both")

root.mainloop()