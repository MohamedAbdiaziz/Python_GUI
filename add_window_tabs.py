from tkinter import *
from tkinter import ttk





root = Tk()

notebook = ttk.Notebook(root)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tetx1")
notebook.add(tab2, text="Tetx2")

notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello World1", width=50, height=20).pack()
Label(tab2, text="Hello World2", width=50, height=20).pack()





root.mainloop()
