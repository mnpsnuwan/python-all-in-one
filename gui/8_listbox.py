from tkinter import *

# listbox = A listing of selectable text items within its own container


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered!")
    for i in food:
        print(i)

    # Single selection mode
    # if listbox.curselection():
    #     print("You have ordered " + listbox.get(listbox.curselection()))
    # else:
    #     print("You haven't selected!")


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

    # Single selection mode
    # if listbox.curselection():
    #     listbox.delete(listbox.curselection())
    #     listbox.config(height=listbox.size())
    # else:
    #     print("You haven't selected deleting item!")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

listbox = Listbox(window,
                  bg='#F7FFDE',
                  width=13,
                  selectmode=MULTIPLE,
                  font=("Cambria", 15))
listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Hotdog")
listbox.insert(4, "Burger")
listbox.insert(5, "Bread")
listbox.insert(6, "Soup")
listbox.insert(7, "Salad")
listbox.pack()
listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,
                   text="Add",
                   command=add)
addButton.pack()

deleteButton = Button(window,
                      text="Delete",
                      command=delete)
deleteButton.pack()

submitButton = Button(window,
                      text="Submit",
                      command=submit)
submitButton.pack()

window.mainloop()

