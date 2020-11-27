import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness
from PIL import Image, ImageTk
import cv2 as cv

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False) # prohibit resizing in both dimensions
root.title("Widget Examples")

# create icon for root window
window_icon = ImageTk.PhotoImage(file='img/google.jpg')
root.iconphoto(False, window_icon)

label = ttk.Label(root, text="Hello, World!", padding=20)
# change font type and size
label.config(font=("Times New Roman", 14))
label.pack()

# read image file with opencv
# img = cv.imread('img/puppy.jpg')
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#
# # convert image array to a TkPhoto object
# img = Image.fromarray(img)
# photo = ImageTk.PhotoImage(img)

# read image file with Image
img = Image.open("img/puppy.jpg")
img = img.resize((128,128))
photo = ImageTk.PhotoImage(img)
label = ttk.Label(root, image=photo, padding=5)
label.pack()

# create compound of text and image
# img = Image.open("img/cloud.jpg")
# img = img.resize((200, 200))
# photo = ImageTk.PhotoImage(img)
# label2 = ttk.Label(root, text="How are you?", image=photo, compound="right")
# label2.config(font=("Arial", 14))
# label2.pack()

greeting = tk.StringVar()
label = ttk.Label(root, padding = 10, textvariable=greeting)
label.pack()

entry = tk.Entry(root, width=15, textvariable=greeting)
entry.pack()

root.mainloop()