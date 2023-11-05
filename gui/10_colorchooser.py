from tkinter import *
from tkinter import colorchooser  # import colorchooser library


def click():
    color = colorchooser.askcolor()
    color_hex = str(color[1])
    # print(color_hex)
    window.config(bg=color_hex)  # Change background color
    # window.config(bg=str(colorchooser.askcolor()[1]))


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.geometry('500x500')
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

button = Button(window,
                command=click,
                text='Choose Color')
button.pack()

window.mainloop()
