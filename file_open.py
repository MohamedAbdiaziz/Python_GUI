# open file and file reading
from tkinter import *
from tkinter import filedialog


def openFile():
    try:

        filepath = filedialog.askopenfilename(title="open files",
                                              filetypes=(("ALL Files", "*.*"),
                                                         ("HTML", "*.html"),
                                                         ("CSS", "*.css")
                                                         ))
        file = open(filepath, "r")
        print(file.read())
        file.close()
    except Exception:
        print("sorry File not found")


window = Tk()
button = Button(text="open File", command=openFile)
button.pack()

window.mainloop()
