from tkinter import *

# widgets = GUI elements: buttons, text-boxes, labels, images
# windows = Serves as a container to hold or contain these widgets


window = Tk()  # initiate an instance of a window
window.geometry("500x500")
window.title("IMATRIXLABS (PVT) LTD GUI")
#
icon = PhotoImage(file='../data/crest.png')
window.iconphoto(True, icon)
# window.config(background="black")
window.config(background="#22211d")

window.mainloop()  # Place window on computer screen, listen for events

