from tkinter import *
from tkinter import messagebox  # import messagebox library


def click():
    # messagebox.showinfo(title="This is an info box",
    #                     message='You are a person')

    # messagebox.showwarning(title="Warning!",
    #                        message='You have a Virus!!!')

    # messagebox.showerror(title="Error!!",
    #                      message='Something Went Wrong!!!!!')

    # if messagebox.askokcancel(title="Ask Ok/Cancel", message="Do you want to proceed?"):
    #     print("You proceeded it! Congratulations!!!")
    # else:
    #     print("You cancelled it! :(")

    # if messagebox.askretrycancel(title="Ask Retry/Cancel", message="Do you want to retry this?"):
    #     print("You Retried it!")
    # else:
    #     print("You cancelled it! :(")

    # if messagebox.askyesno(title="Ask Yes/No", message="Do you like Ice Cream?"):
    #     print("Yes I like Ice Cream very much!")
    # else:
    #     print("No I don't like Ice Cream")

    # answer = messagebox.askquestion(title="Ask Question", message="Do you like pie?")
    # if answer == "yes":
    #     print("I also like pie!")
    # else:
    #     print("Why don't you like pie? :(")

    answer = messagebox.askyesnocancel(title="Ask Yes/No/Cancel", message="Do you like to Code?", icon='info')
    if answer is None:
        print("Huh, you cancelled it!")
    elif answer:
        print("I like to Code too!")
    else:
        print("Why are you watching a video on coding?")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

button = Button(window,
                command=click,
                text='Click Me!')
button.pack()

window.mainloop()

