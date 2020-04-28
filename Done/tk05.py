import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import messagebox

mainFrame = tk.Tk()
label1 = Label(mainFrame, text="Nom")
label1.grid(row=0, column=0)

entry1 = Entry(mainFrame, bd=5)
entry1.grid(row=0, column=1)

label2 = Label(mainFrame, text="Prenom")
label2.grid(row=1, column=0)

entry2 = Entry(mainFrame, bd=5)
entry2.grid(row=1, column=1)


def btnCallBack():
    str = "Les valeurs sont\n - nom:{0},\n - prenom:{1}".format(entry1.get(), entry2.get())
    messagebox.showinfo("Les valeurs ", str)


button = tk.Button(mainFrame, text="Voir", command=btnCallBack)

button.grid(row=2, column=0, columnspan=2)

mainFrame.mainloop()
