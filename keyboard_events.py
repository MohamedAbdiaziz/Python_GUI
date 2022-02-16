from tkinter import *


def keysFunc(event):
    # print("you pressed ", event.keysym)
    label.config(text=event.keysym)


root = Tk()
root.bind("<Key>", keysFunc)
label = Label(root, font=("Helvetica", 100))
label.pack()
root.mainloop()
