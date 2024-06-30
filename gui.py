'''
EXAMPLE TKINTER GUI

'''


#two modules, 1st loads tk library
# 2nd is a submodule of tkinter
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

'''Sets up the main app window and gives it a title'''
root = Tk()
root.title("Foot to Meter Converter")

'''creating frame widget to hold contents'''
s = ttk.Style()
s.configure('Danger.TFrame', backgroud='red', borderwidth=5, relief='raised')
mainframe = ttk.Frame(root, width=50, height=50, style='Danger.TFrame')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

'''Creating the entry widget for input'''
feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W,)

ttk.Label(mainframe, textvariable=meters).grid(column=10, row=5, sticky=(W, E))
ttk.Label(mainframe, text="Input measurement in feet").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()