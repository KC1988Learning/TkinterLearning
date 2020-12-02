import tkinter as tk
from tkinter import ttk
from tutorial.window import set_dpi_awareness
from tkinter import font

set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #################### configuration ###############################
        # set font size of default text
        font.nametofont("TkDefaultFont").configure(size=15)

        # set column to take up entire horizontal space with expansion
        self.columnconfigure(0, weight=1)

        # create root title
        self.title("Distance Converter")

        # create frames dictionary
        self.frames = dict()
        ##################################################################

        # create an inner container for better space control
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")
        #
        # # create stacked frames inside the inner container
        # # later frame stacked on top of the earlier ones
        # feet_to_metres = FeetToMetres(container, self)
        # feet_to_metres.grid(row=0, column=0, sticky="NSEW")
        #
        # metres_to_feet = MetresToFeet(container, self)
        # metres_to_feet.grid(row=0, column=0, sticky="NSEW")
        #
        # # assigning frame instances to the corresponding frame class in the dictionary
        # self.frames[FeetToMetres] = feet_to_metres
        # self.frames[MetresToFeet] = metres_to_feet

        # the three blocks above can be further simplified as
        for FrameClass in (MetresToFeet, FeetToMetres):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        # choose which frame to raise at the beginning
        self.show_frames(FeetToMetres)

        # event binding to window
        # self.bind("<Return>", feet_to_metres.calculate)
        # self.bind("<KP_Enter>", feet_to_metres.calculate)

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()

class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        # instantiate variables
        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()

        # instantiate widget elements
        metres_label = ttk.Label(self, text="Metres: ")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Convert", command=self.calculate)
        switch_button = ttk.Button(self, text="Switch", command=lambda: controller.show_frames(FeetToMetres))

        ################################################################################################
        # position the widget elements
        ################################################################################################
        metres_label.grid(row=0, column=0, sticky="W")
        metres_input.grid(row=0, column=1, sticky="W")
        metres_input.focus()

        feet_label.grid(row=1, column=0, sticky="W")
        feet_display.grid(row=1, column=1, sticky="W")

        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")
        switch_button.grid(row=3, column=0, columnspan=2, sticky="EW")

        # set equal padding for all widget elements
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)
        ################################################################################################

    def calculate(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        ################################## create variables ###########################################
        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()

        ###################################### create widget ##########################################
        feet_label = ttk.Label(self, text="Feet: ")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 15))
        metres_label = ttk.Label(self, text="Metres: ")
        metres_display = ttk.Label(self, textvariable=self.metres_value)
        calc_button = ttk.Button(self, text="Convert", command=self.calculate)
        switch_button = ttk.Button(self, text="Switch", command=lambda: controller.show_frames(MetresToFeet))

        ##################################### position widgets ########################################
        feet_label.grid(row=0, column=0, sticky="W")
        feet_input.grid(row=0, column=1, sticky="W")
        metres_label.grid(row=1, column=0, sticky="W")
        metres_display.grid(row=1, column=1, sticky="W")
        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")
        switch_button.grid(row=3, column=0, columnspan=2, sticky="EW")

        ################################# configure widgets properties ################################
        # 1. set equal paddings for all widgets
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

        # 2. make input the focus
        feet_input.focus()

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet * 0.3048
            self.metres_value.set(f"{metres:.3f}")
        except:
            pass

root = DistanceConverter()
root.mainloop()