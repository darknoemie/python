import tkinter as tk
from tkinter import Listbox
from tkinter import Scrollbar

mainFrame = tk.Tk()

compteur = 0

# def listboxCallback():
#     sys.stdout.write("Ajout d'un item")

scrollbar = Scrollbar(mainFrame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = Listbox(mainFrame, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

""" Fonction callback """


def addCallBack():
    global compteur
    compteur += 1
    listbox.insert(tk.END, "item n{0}".format(compteur))
    # messagebox.showinfo( "Titre Message", "Texte du message")


listbox.pack()

button = tk.Button(mainFrame, text="ajoute un item", command=addCallBack)

button.pack()
mainFrame.mainloop()
