from tkinter import *

def display():

    if (x.get()==1):
        print("welcome")
    else:
        print("oky!, good")

window = Tk()
x = IntVar()
chek_button = Checkbutton(window, text="some time ",
                          variable=x,
                          offvalue=0,
                          onvalue=1,
                          command=display
                          )
chek_button.pack()

window.mainloop()
