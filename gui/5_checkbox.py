from tkinter import *


def display():
    if click.get():
        print("You agreed!")
    else:
        print("You don't agreed!")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

click = BooleanVar()
# click = StringVar()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
photo = PhotoImage(file='../data/images/python.png')
window.iconphoto(True, icon)

check_button = Checkbutton(window,
                           text="I agree to something!",
                           variable=click,
                           onvalue=True,
                           offvalue=False,
                           # onvalue="YES",
                           # offvalue="NO",
                           command=display,
                           font=('Arial', 18),
                           padx=25,
                           pady=10,
                           fg="#00FFF0",
                           bg="black",
                           activeforeground="#00FFF0",
                           activebackground="black",
                           image=photo,
                           compound='left')
check_button.pack()

window.mainloop()

