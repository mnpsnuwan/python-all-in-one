import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Pick a color ... or else")
    text_area.config(fg=str(color[1]))


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("{} - Untitled".format(title))
    text_area.delete(1.0, END)


def open_file():
    text_file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title("{} - {}".format(title, os.path.basename(text_file)))
        text_area.delete(1.0, END)

        text_file = open(text_file, "r")

        text_area.insert(1.0, text_file.read())

    except Exception:
        print("Couldn't read file!")

    finally:
        text_file.close()


def save_file():
    text_file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                             defaultextension=".txt",
                                             filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", "*.txt")])

    if text_file is None:
        return
    else:
        try:
            window.title("{} - {}".format(title, os.path.basename(text_file)))
            text_file = open(text_file, "w")

            text_file.write(text_area.get(1.0, END))

        except Exception:
            print("Couldn't save file!")

        finally:
            text_file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this text editor", "Text Editor\n\nCopyright © 2023 {}.".format(title))


def quit_or_exit():
    window.destroy()


title = "IMATRIXLABS (PVT) LTD"
file = None
window_width = 500
window_height = 500

window = Tk()
window.title("Text Editor - " + title)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

font_name = StringVar(window)
font_name.set("Cambria")

font_size = StringVar(window)
font_size.set("13")

text_area = Text(window, bg="#ffe", font=(font_name.get(), font_size.get()))
text_area.pack()

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set, xscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

f_color_button = Button(frame, text="font-color", command=change_color)
f_color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=2)

size_box = Spinbox(frame, command=change_font, textvariable=font_size, from_=1, to=100)
size_box.grid(row=0, column=3)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_or_exit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Cut", command=cut)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


window.mainloop()


