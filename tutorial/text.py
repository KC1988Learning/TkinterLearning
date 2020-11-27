import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import set_dpi_awareness

set_dpi_awareness()

def print_text():
    if text["state"]=="disabled":
        text["state"]="normal"
        text.insert("1.0", "Start typing here!")
        btn_text.set("Snap content")
    else:
        # get text content from 1st row 0th index all the way to the end

        text_content = text.get("1.0", "end")
        print(text_content)

################# SET MAIN WINDOW PROPERTY #################
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text Example")

icon = ImageTk.PhotoImage(file="img/google.jpg")
root.iconphoto(False, icon)
############################################################

# height = 8: total of 8 rows of text available
text = tk.Text(root, height=8)
text.pack()


text["state"]="disabled" # opposite if "disabled"

btn_text = tk.StringVar()
btn_text.set("Start")
btn = ttk.Button(root, textvariable=btn_text, command=print_text)
btn.pack()

root.mainloop()