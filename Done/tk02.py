import tkinter as tk
from tkinter import messagebox


mainFrame= tk.Tk()

""" Fonction callback """
def helloCallBack():
    messagebox.showinfo( "Titre Message", "Texte du message")

button = tk.Button(mainFrame, text ="Btn clic", command = helloCallBack)

button.pack()
mainFrame.mainloop()