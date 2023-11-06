from tkinter import *


def move_up(event):
    canvas.move(car, 0, -10)


def move_left(event):
    canvas.move(car, -10, 0)


def move_down(event):
    canvas.move(car, 0, 10)


def move_right(event):
    canvas.move(car, 10, 0)


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

canvas = Canvas(window, width=450, height=450, bg="light yellow")
canvas.pack()

car = canvas.create_image(0, 0, image=my_car, anchor=NW)

window.mainloop()
