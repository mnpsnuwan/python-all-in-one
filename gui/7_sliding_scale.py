from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

hotLabel = Label(text='🔥')
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=450,
              orient=VERTICAL,  # Orientation of scale
              font=('Console', 13),
              tickinterval=10,  # Adds numeric indicators for value
              showvalue=False,  # Hide current value
              troughcolor='#00FFF0',
              fg='#FFF000',
              bg='#000000'
              )

scale.set(((scale['from']-scale['to'])/2+scale['to']))
scale.pack()

coldLabel = Label(text='❄️')
coldLabel.pack()

button = Button(window,
                text="submit",
                command=submit)
button.pack()

window.mainloop()

