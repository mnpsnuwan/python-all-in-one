from tkinter import *


def drag_start(event):
    widget = event.widget  # With this line compatible for each and every label

    # label1.startX = event.x
    # label1.startY = event.y

    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")
window.geometry("500x500")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

label1 = Label(window, bg="red", width=10, height=5)
label1.place(x=0, y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=250, y=250)

label1.bind("<Button-1>", drag_start)
label1.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()
