from tkinter import *
from time import *


def update():
    time_string = strftime("%H:%M:%S")
    label.config(text=time_string)
    label.after(1000, update)
    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B/%d/%Y")
    date_label.config(text=date_string)


root = Tk()

label = Label(root, font=("Helvetica", 100), bg="black", fg="#00ff00")
label.pack()

day_label = Label(root, font=("Ink free", 30))
day_label.pack()

date_label = Label(root, font=("Ink free", 30))
date_label.pack()

update()
root.resizable(False, False)
root.mainloop()
