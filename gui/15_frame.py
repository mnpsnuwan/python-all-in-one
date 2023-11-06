from tkinter import *

# Frame = A rectangular container to group and hold widgets

title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

frame = Frame(window,
              bg="light yellow",
              bd=3,
              relief=SUNKEN)
# frame.pack()
frame.place(x=100, y=100)

Button(frame,
       text="W",
       font=("Console", 20),
       width=3).pack(side=TOP)
Button(frame,
       text="A",
       font=("Console", 20),
       width=3).pack(side=LEFT)
Button(frame,
       text="S",
       font=("Console", 20),
       width=3).pack(side=LEFT)
Button(frame,
       text="D",
       font=("Console", 20),
       width=3).pack(side=LEFT)


window.mainloop()
