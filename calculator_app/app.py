import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tutorial.window import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.title("Distance Calculator")

# get Tkinter default font, and then configure the size
# applied to text in the application, but not text in field
# therefore you still need to configure font size of text in field separately
font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(index=0, weight=1)
main = ttk.Frame(root, padding=(30,15))
main.grid(row=0, column=0)

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        print(f"{metres} metres is equal to {feet:.3f} feet.")
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


# output_value = tk.DoubleVar()
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here.")

metres_label = ttk.Label(main, text="Metres: ")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)
metres_input.grid(row=0, column=1, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(row=1, column=0, sticky="W", padx=5, pady=5)
feet_display.grid(row=1, column=1, sticky="EW", padx=5, pady=5)

# it is noted that there are multiple widgets in the main frame with equal padding
# remove duplication using winfo_children (stands for widget into children)
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")

# bind the event <Return> : press middle Enter key and
# event <KP_Enter> : press Enter key on number key pad
# trigger calculate_feet when the event occurs
metres_input.bind("<Return>", calculate_feet)
metres_input.bind("<KP_Enter>", calculate_feet)

root.mainloop()