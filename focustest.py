
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

# Add a text field that responds to where focus has been placed
foc_val = StringVar()
foc_val.set("No focus")
foc_view = ttk.Entry(frame, width = 7, textvariable = foc_val)
foc_view.grid(column = 1, row = 1, sticky = (W, E))

# Focus commands
foc_view.bind("<FocusIn>", foc_val.set("Focus in"))
foc_view.bind("<FocusOut>", foc_val.set("Focus out"))

# Resize widgets inside frame
for child in frame.winfo_children():
	child.grid_configure(padx = 5, pady = 5)


root.mainloop()
