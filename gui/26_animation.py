from tkinter import *
import time


WIDTH = 450
HEIGHT = 450

x_velocity = 3
y_velocity = 2

title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")
window.geometry("475x475")

icon = PhotoImage(file='../data/images/crest.png')
background_image = PhotoImage(file='../data/images/universe.png')
ufo_image = PhotoImage(file='../data/images/ufo.png')

window.iconphoto(True, icon)

canvas = Canvas(window, width=WIDTH,
                height=HEIGHT,
                bg="light yellow")
canvas.pack()

background = canvas.create_image(0, 0, image=background_image, anchor=NW)
ufo = canvas.create_image(0, 0, image=ufo_image, anchor=NW)

ufo_image_height = ufo_image.height()
ufo_image_width = ufo_image.width()

while True:
    coordinates = canvas.coords(ufo)
    print(coordinates)
    if coordinates[0] >= (WIDTH-ufo_image_width) or coordinates[0] < 0:
        x_velocity = -x_velocity
    if coordinates[1] >= (HEIGHT-ufo_image_height) or coordinates[1] < 0:
        y_velocity = -y_velocity
    canvas.move(ufo, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
