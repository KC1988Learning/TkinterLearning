import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

set_dpi_awareness()

# create frame without custom class
# root = tk.Tk()
# frame = ttk.Frame(root).pack()
# label = ttk.Label(frame, text="Enter your name: ")
# label.pack()
#
# root.mainloop()

# create root with custom class
class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        UserInputFrame(self).pack()

# create frame with custom class
class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container) # container can be a root, or other frame that contains the current frame

        # create a label
        label = ttk.Label(self, text="Enter your name: ")

        # create an entry field
        self.user_input = tk.StringVar()
        entry = ttk.Entry(self, width=15, textvariable=self.user_input)
        entry.focus()

        # create a button
        btn = ttk.Button(self, text="Click me", command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        btn.pack(side="left")

    def greet(self):
        print(f"Hello {self.user_input.get() or 'World'}!")


root = HelloWorld()
root.mainloop()

