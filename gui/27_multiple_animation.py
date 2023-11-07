from tkinter import *
from Ball import *
import time

WIDTH = 450
HEIGHT = 450

title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")
window.geometry("475x475")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

canvas = Canvas(window, width=WIDTH,
                height=HEIGHT,
                bg="light blue")
canvas.pack()

volly_ball = Ball()
volly_ball.__int__(canvas, 0, 0, 50, 1, 1, "white")

tennis_ball = Ball()
tennis_ball.__int__(canvas, 0, 0, 20, 4, 3, "yellow")

basket_ball = Ball()
basket_ball.__int__(canvas, 30, 30, 100, 5, 4, "orange")

magic_ball = Ball()
magic_ball.__int__(canvas, 10, 10, 20, 10, 9, "purple")


while True:
    volly_ball.move()
    tennis_ball.move()
    basket_ball.move()
    magic_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
