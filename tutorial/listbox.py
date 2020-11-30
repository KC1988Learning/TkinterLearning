import tkinter as tk
from tkinter import ttk
from window import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Listbox")

programming_languages=("C", "Go", "JavaScript", "Perl", "Python", "Rust")

# initialize langs with the value option
langs = tk.StringVar(value=programming_languages)

# listbox is a tk widget, is not under ttk - themable tkinter widget
# use listvariable as it takes in a tuple, instead of a string
# set selectmode to extended for multiple item selection
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")

# an alternative to set the selectmode
# langs_select = tk.Listbox(root, listvariable=langs, height=6)
# langs_select["selectmode"]="extended" # "browse" for unique selection

langs_select.pack()

# event handler of printing out selected items in the listbox
def handle_selection_change(event):
    # return list of indices of current selected items
    selected_indices = langs_select.curselection()

    # iterate over selected indices and print out the item
    for i in selected_indices:
        print(langs_select.get(i))

# bind the event listener of "Selecting items" to the widge
# and apply event handler handle_selection_change when the event occurs
langs_select.bind("<<ListboxSelect>>", handle_selection_change)
root.mainloop()