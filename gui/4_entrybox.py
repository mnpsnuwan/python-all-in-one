from tkinter import *

# entry widget = Textbox that accepts a single line of user input


def submit():
    text = entry.get()
    print("You submitted ",  text)
    # entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


title = "IMATRIXLABS (PVT) LTD"

window = Tk()
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
photo = PhotoImage(file='../data/images/icon.png')
window.iconphoto(True, icon)

# Entry
entry = Entry(window,
              font=('Comic Sans', 20),
              fg='#00FFF0',
              bg='#000C00',
              show='*')
entry.insert(0, "IMATRIXLABS")
entry.pack(side=LEFT)

# Submit button
submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack(side=RIGHT)

# Delete button
delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side=RIGHT)

# Backspace button
backspace_button = Button(window,
                          text="Backspace",
                          command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()

