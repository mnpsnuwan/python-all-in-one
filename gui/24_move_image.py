from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)


def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)


def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")
window.geometry("500x500")

icon = PhotoImage(file='../data/images/crest.png')
my_car = PhotoImage(file='../data/images/ferrari.png')

window.iconphoto(True, icon)

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

label = Label(window, image=my_car)
label.place(x=0, y=0)

window.mainloop()
