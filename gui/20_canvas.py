from tkinter import *

# canvas = widget that is used to draw graphs, plots, images in a window

title = "IMATRIXLABS (PVT) LTD"

window = Tk()

# window.geometry("400x400")
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

points = [250, 211, 211, 234, 211, 279, 250, 301, 289, 279, 289, 234]

canvas = Canvas(window, height=500, width=500)
# blue_line = canvas.create_line(0, 0, 500, 500, fill="blue", width=4)
# red_line = canvas.create_line(0, 500, 500, 0, fill="red", width=4)
# canvas.create_rectangle(20, 20, 480, 480, fill="purple")
canvas.create_polygon(250, 0, 500, 500, 0, 500,  fill="indigo",
                      outline="black", width=2)  # ((x,y),(x,y),(x,y), ...) clockwise
canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=180, extent=180, fill="green")
canvas.create_polygon(points, fill="orange", outline="white", width=3)  # ((x,y), (x,y), ...) anticlockwise
canvas.create_oval(227, 234, 273, 280, fill="red", outline="blue", width=2)
canvas.pack()

window.mainloop()
