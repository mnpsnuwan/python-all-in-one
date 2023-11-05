from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        initialfile="textFile.txt",
        initialdir="../data",
        title="Open file window!",
        filetypes=[
            ("text files", "*.txt"),
            ("HTML", "*.html"),
            ("all files", "*.*")]
    )
    if file is None:
        return

    file_text = str(text.get("1.0", END))
    # file_text = input("Enter some text to write in the file: ")  # Getting console input after saving the file
    file.write(file_text)
    file.close()


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

text = Text(window)
text.pack()

button = Button(window,
                command=save_file,
                text='Save')
button.pack()

window.mainloop()

