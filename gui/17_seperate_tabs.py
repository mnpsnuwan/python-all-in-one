from tkinter import *
from tkinter import ttk

title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.geometry("400x400")
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

notebook = ttk.Notebook(window)  # This widget manages a collection of windows/displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")  # expand to fill any space not otherwise | fill space on x-axis and y-axis

Label(tab1, text="This is Tab 1", width=50, height=20).pack()
Label(tab2, text="This is Tab 2", width=50, height=20).pack()

window.mainloop()
