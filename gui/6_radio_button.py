from tkinter import *

# radio button = Similar to checkbox, but you can only select one from a group

food = ["🍕 Pizza", "🍔 Burger", "🌭 Hotdog"]


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered burger!")
    elif x.get() == 2:
        print("You ordered hotdog!")
    else:
        print("Huh?")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

x = IntVar()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
photo = PhotoImage(file='../data/images/python.png')
window.iconphoto(True, icon)

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # adds text to radio buttons
                               variable=x,  # groups radio buttons together if they share the variable
                               value=index,  # assigns each radio button a different value
                               font=('Impact', 25),
                               fg="#00FFF0",
                               bg="black",
                               activeforeground="#00FFF0",
                               activebackground="black",
                               padx=25,  # add padding on x-axis
                               pady=10,
                               indicatoron=0,  # eliminate circle indicators
                               command=order,  # set command of radio button to function
                               width=15)
    radio_button.pack(anchor=W)

window.mainloop()

