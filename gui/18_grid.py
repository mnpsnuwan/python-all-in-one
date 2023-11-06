from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure in a parent

title = "IMATRIXLABS (PVT) LTD"

window = Tk()

window.geometry("400x400")
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
window.iconphoto(True, icon)

title_label = Label(window, text="Contact Info", font=("Calibri", 25))
title_label.grid(row=0, column=0, columnspan=3)

first_name_label = Label(window, text="First Name: ", width=25)
first_name_label.grid(row=1, column=0)
first_name_entry = Entry(window, width=25)
first_name_entry.grid(row=1, column=1)

last_name_label = Label(window, text="Last Name: ")
last_name_label.grid(row=2, column=0)
last_name_entry = Entry(window, width=25)
last_name_entry.grid(row=2, column=1)

email_label = Label(window, text="Email: ")
email_label.grid(row=3, column=0)
email_entry = Entry(window, width=25)
email_entry.grid(row=3, column=1)

number_label = Label(window, text="Number of members: ")
number_label.grid(row=4, column=0)
number_entry = Entry(window, width=25)
number_entry.grid(row=4, column=1)
number_button = Button(window, text="<>")
number_button.grid(row=4, column=2)

frame1 = Frame(window)
frame1.grid(row=5, column=0)

frame2 = Frame(window)
frame2.grid(row=5, column=1, columnspan=3)  # columnspan = between 3 columns

update_button = Button(frame1, text="Update", width=6)
update_button.grid(row=0, column=0)
reset_button = Button(frame1, text="Reset", width=6)
reset_button.grid(row=0, column=1)
cancel_button = Button(frame1, text="Cancel", width=6)
cancel_button.grid(row=0, column=2)
save_button = Button(frame2, text="Save", width=6)
save_button.grid(row=0, column=3)
export_button = Button(frame2, text="Export", width=6)
export_button.grid(row=0, column=4)
import_button = Button(frame2, text="Import", width=6)
import_button.grid(row=0, column=5)

window.mainloop()


#             ||     col 0     ||     col 1     ||     col 2     ||
#   ||  row 0 || (row 0, col 0) | (row 0, col 1) | (row 0, col 2) |
#   ||  row 1 || (row 1, col 0) | (row 1, col 1) | (row 1, col 2) | =>>>
#   ||  row 2 || (row 2, col 0) | (row 2, col 1) | (row 2, col 2) |
#   ||  row 3 || (row 3, col 0) | (row 3, col 1) | (row 3, col 2) |

