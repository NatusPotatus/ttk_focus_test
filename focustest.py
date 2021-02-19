
# Call tkinter tools
from tkinter import *
from tkinter import ttk

"""
TODO:
Have the entry field change when it gains and loses focus from the user.
Add different widgets that can 'gain' focus.
Change the entry text depending on which widget has focus.
"""

# Develop the window and frame
root = Tk()
root.title("Focus Test")
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

frame = ttk.Frame(root, padding = "1 1 1 1")
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))

# Resizes columns in frame
for col in range(1, 3):
	frame.columnconfigure(col, weight = 1)

# Resizes rows in frame
for row in range(1, 3):
	frame.rowconfigure(row, weight = 1)

# Add response label
foc_labvar = StringVar()
foc_labvar.set("No focus")
foc_lab = ttk.Label(frame, width = 7, textvariable = foc_labvar)
foc_lab.grid(column = 2, row = 2, sticky = (W, E))

# Add entry box
foc_entvar = StringVar()
foc_entvar.set("Entry widget")
foc_ent = ttk.Entry(frame, width = 7, textvariable = foc_entvar)
foc_ent.grid(column = 1, row = 1, sticky = (W, E))

# Add button
foc_butvar = StringVar()
foc_butvar.set("Button widget")
foc_but = ttk.Button(frame, width = 7, textvariable = foc_butvar)
foc_but.grid(column = 2, row = 1, sticky = (W, E))

# Focus commands
def focus(event):
	focused_widget = frame.focus_get()
	foc_labvar.set(focused_widget, "has focus")
	print(focused_widget, "has focus")

# Bind mouse click to run focus command
root.bind("<Button-1>", focus)

# Resize widgets inside frame
for child in frame.winfo_children():
	child.grid_configure(padx = 5, pady = 5)


root.mainloop()
