import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness
from PIL import ImageTk

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.title("Scroll bar")

root_icon = ImageTk.PhotoImage(file="img/google.jpg")
root.iconphoto(False, root_icon)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = tk.Text(root, height=10)
text.grid(row=0, column=0, sticky="EWN")
text.insert("1.0", "Enter your comment here......")

# command = text.yview: changes vertical postion of the text when scrolling
text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text_scroll.grid(row=0, column=1, sticky="NS")

# link the vertical position of text to the scroll bar
text["yscrollcommand"]=text_scroll.set

root.mainloop()
