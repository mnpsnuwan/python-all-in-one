from tkinter import *


def create_window():
    # new_window = Toplevel()  # New window 'on top' of other windows, linked to a 'bottom' window
    new_window = Tk()

    window.destroy()  # Close old window

    new_window.title(title + " GUI")
    new_window.geometry("250x250")

    label = Label(new_window, text="This is newly created window")
    label.pack()

    button_new = Button(new_window, text="Click Me!", fg="#ccc")
    button_new.pack()

    new_window.mainloop()


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.geometry("400x400")
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

button = Button(window, text="Open New Window", command=create_window)
button.pack()

window.mainloop()
