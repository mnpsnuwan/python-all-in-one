from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks = 10
    x = 0
    while x < tasks:
        time.sleep(1)
        bar['value'] += 10
        x += 1
        percent.set(str(int((x/tasks)*100)) + "%")
        text.set(str(x) + "/" + str(tasks) + "tasks completed!")
        window.update_idletasks()
    print("Started!!")


title = "IMATRIXLABS (PVT) LTD"

window = Tk()

percent = StringVar()
text = StringVar()

window.geometry("400x400")
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent)
percent_label.pack()

task_label = Label(window, textvariable=text)
task_label.pack()

button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()
