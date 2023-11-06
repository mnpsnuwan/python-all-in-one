from tkinter import *


def open_file():
    print("File has been opened!")


def save_file():
    print("File has been saved!")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("You pasted some text!")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,
                 tearoff=0,
                 font=("My Boli", 10))
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="📂Open",
                      command=open_file)
file_menu.add_command(label="💾Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="🛑Exit", command=quit)

edit_menu = Menu(menu_bar,
                 tearoff=0,
                 font=("My Boli", 10))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()

