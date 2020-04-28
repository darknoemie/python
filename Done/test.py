import tkinter as tk
from tkinter import messagebox
from tkinter import Label
from tkinter import Entry
from tkinter import Text
from tkinter import Listbox
from tkinter import Scrollbar

from crud import readall

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.fields = ['id', 'mnemo', 'raison', 'adresse1', 'adresse2', 'codeinsee']
        self.create_widgets()
        self.loaddata()

    def create_widgets(self):

        for f in self.fields:
            str = f

        label1 = Label(self, text="Mnemo")
        label1.grid(row=0, column=0)

        self.mnemo = Entry(self, bd=5)
        self.mnemo.grid(row=0, column=1)

        label2 = Label(self, text="Raison")
        label2.grid(row=1, column=0)

        self.raison = Entry(self, bd=5)
        self.raison.grid(row=1, column=1)

        label3 = Label(self, text="Adresse")
        label3.grid(row=2, column=0)

        self.adresse1 = Entry(self, bd=5)
        self.adresse1.grid(row=2, column=1)

        label4 = Label(self, text="")
        label4.grid(row=3, column=0)

        self.adresse2 = Entry(self, bd=5)
        self.adresse2.grid(row=3, column=1)

        label5 = Label(self, text="Code insee")
        label5.grid(row=4, column=0)

        self.codeinsee = Entry(self, bd=5)
        self.codeinsee.grid(row=4, column=1)
        # columnspan=Number

        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=0, column=3, rowspan=5)
        # scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

        self.listbox = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.grid(row=0, column=2, rowspan=5)

        self.btnInsert = tk.Button(self)
        self.btnInsert.grid(row=6, column=0)
        self.btnInsert["text"] = "Insert"
        self.btnInsert["command"] = self.insert

        self.quit = tk.Button(self, text="QUIT", fg="grey", command=self.master.destroy)
        self.quit.grid(row=6, column=1)

    def insert(self):
        pass

    def loaddata(self):
        rows = readall()
        for row in rows:
            str = row
            self.listbox.insert(tk.END, str)


root = tk.Tk()
app = Application(master=root)
app.mainloop()