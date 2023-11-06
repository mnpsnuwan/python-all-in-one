from tkinter import *

# canvas = widget that is used to draw graphs, plots, images in a window


def do_something(event):
    coordinates_x = str(event.x)
    coordinates_y = str(event.y)
    print("Mouse coordinates: " + coordinates_x, ", " + coordinates_y)


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")
window.geometry("500x500")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

# window.bind("<Button-1>", do_something)  # left mouse click
# window.bind("<Button-2>", do_something)  # mouse wheel
# window.bind("<Button-3>", do_something)  # right mouse click
# window.bind("<ButtonRelease>", do_something)
# window.bind("<Enter>", do_something)  # Enter the window
# window.bind("<Leave>", do_something)
window.bind("<Motion>", do_something)

window.mainloop()
