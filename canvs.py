from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500)

# canvas.create_line(0, 0, 500, 500, fill="Blue", width=5)
# canvas.create_line(500, 0, 0, 500, fill="Blue", width=5)
# canvas.create_line(250, 0, 250, 500, fill="white", width=5)

canvas.create_rectangle(400, 400, 60, 60)

canvas.pack()

root.mainloop()
