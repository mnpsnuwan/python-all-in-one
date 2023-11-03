from tkinter import *

# button = An area widget that holds button within a window
count = 0


def click():
    global count
    count += 1
    print("You clicked the button", count, "times")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()
window.title(title + " GUI")

icon = PhotoImage(file='../data/crest.png')
photo = PhotoImage(file='../data/icon.png')
window.iconphoto(True, icon)

# button
button = Button(window,
                text='Click Me!',
                command=click,
                font=('Comic Sans', 25),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                # state=DISABLED,
                state=ACTIVE,
                image=photo,
                compound='left',
                padx=25,
                pady=25,
                border='8')

button.pack()

window.mainloop()

