from tkinter import *
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(
        initialdir="../data",
        title="Open file window!",
        filetypes=(("text files", "*.txt"), ("all files", "*.*"))
    )
    # print(file_path)
    file = open(file_path, 'r')
    print(file.read())
    file.close()


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

button = Button(window,
                command=open_file,
                text='Open')
button.pack()

window.mainloop()





