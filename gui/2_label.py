from tkinter import *

# label = An area widget that holds text and/or an image within a window

title = "IMATRIXLABS (PVT) LTD"
window = Tk()
window.title(title + " GUI")

icon = PhotoImage(file='../data/images/crest.png')
photo = PhotoImage(file='../data/images/FLogo.png')
window.iconphoto(True, icon)

# Label
label = Label(window,
              text=title,
              font=('Arial', 40, 'bold'),
              fg='#31C6D4',
              bg='black',
              relief=RAISED,
              bd=8,
              padx=25,
              pady=25,
              image=photo,
              compound='bottom')
# label.place(x=0, y=0)  # Can place anywhere using x,y
label.pack()

window.mainloop()

