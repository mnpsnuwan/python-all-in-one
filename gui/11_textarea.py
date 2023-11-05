from tkinter import *

# text widget = Functions like a text area, you can enter multiple lines of text


def submit():
    input_text = text.get("1.0", END)
    print(input_text)


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 15),
            height=8,
            width=20,
            pady=20,
            padx=20,
            fg="purple")
text.pack()

button = Button(window,
                command=submit,
                text='Submit')
button.pack()

window.mainloop()





