from tkinter import *
# from tkinter import filedialog

def openFile():
    print("good1")
def saveFile():
    print("good2")
def exitFile():
    window.destroy()
    print("good3")

window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="open", font=("arial 20 bold"), command=openFile)
file_menu.add_command(label="sava", font=("arial 20 bold"), command=saveFile)
file_menu.add_separator()
file_menu.add_command(label="exit", font=("arial 20 bold"), command=exitFile)
window.resizable(False, False)
window.mainloop()
