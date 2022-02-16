from tkinter import *


def keysFunc(event):
    # print("you pressed ", event.keysym)
    label.config(text=str(event.x)+","+str(event.y))


root = Tk()
# root.bind("<Button-1>", keysFunc)     #left mouse click
# root.bind("<Button-2>", keysFunc)     #scroll wheel
# root.bind("<Button-3>", keysFunc)     #right mouse click
root.bind("<ButtonRelease>", keysFunc)
# root.bind("<Enter>", keysFunc)    #enter the Window
# root.bind("<Leave>", keysFunc)    #Leave the window
# root.bind("<Motion>", keysFunc)     #where the mouse moved
label = Label(root, font=("Helvetica", 100))
label.pack()
root.geometry("1000x700")
root.mainloop()
