from tkinter import *
from tkinter.ttk import *
import time


def download():

    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percentage.set(str(int((download/GB)*100))+"%")
        tasks.set(str(download)+"/"+str(GB)+" MB successed ")
        root.update_idletasks()
    print("Complete")


root = Tk()
percentage = StringVar()
tasks = StringVar()
bar = Progressbar(root, orient=HORIZONTAL, length=300)
bar.pack(pady=10, padx=10)

Label(root, textvariable=percentage).pack()
Label(root, textvariable=tasks).pack()

Button(text="download", command=download).pack()
root.mainloop()
