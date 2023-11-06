from tkinter import *

# canvas = widget that is used to draw graphs, plots, images in a window


def do_something(event):
    key = event.keysym
    print("You pressed: " + key)
    label.config(text=key)


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

window.bind(
    "<Key>",  # All key function
    # "<Return>",  # Enter keypress function
    do_something)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
