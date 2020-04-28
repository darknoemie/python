import tkinter as tk
from tkinter import Label
from tkinter import Radiobutton


def sel():
    selection = "Vous avez sélectionné l'option " + str(var.get())
    label.config(text=selection)


mainFrame = tk.Tk()
var = tk.IntVar()
var2 = tk.IntVar()
R1 = Radiobutton(mainFrame, text="Option 1", variable=var, value=1,
                 command=sel)
R1.pack(anchor=tk.W)

R2 = Radiobutton(mainFrame, text="Option 2", variable=var, value=2,
                 command=sel)
R2.pack(anchor=tk.W)

R3 = Radiobutton(mainFrame, text="Option 3", variable=var, value=3,
                 command=sel)
R3.pack(anchor=tk.W)
R4 = Radiobutton(mainFrame, text="Option 3", variable=var, value=3,
                 command=sel)
R4.pack(anchor=tk.W)
R5 = Radiobutton(mainFrame, text="Option 3", variable=var2, value=1,
                 command=sel)
R5.pack(anchor=tk.W)

label = Label(mainFrame)
label.pack()
mainFrame.mainloop()
