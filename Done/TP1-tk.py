import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import END
from _datetime import datetime
from random import random

"""
TP: TK

Réaliser un formulaire de saisie lancement d'un test
Il faut saisir le n° de test
La date se remplit automatiquement

Générer de manière aléatoire les valeurs du test.
Sauvegarder les valeurs dans un fichier au format CSV

"""

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
       
    def generate_values(self):
        self.listofvalues = []
        for i in range(10):
            x = int(random() * 1000)    
            print (x) 
            self.listofvalues.append(x)
            
    def runTest(self):
        s ="Test {0} , lancé le {1}".format(self.numerotest.get(),self.datetest.get())
        print(s)  
        self.generate_values()  
        
    def saveTest(self):
        # Ouvrir un fichier en écriture
        f = open(self.filename, 'w')

        # Ecrire dans le fichier
        for x in self.listofvalues:
          f.write(repr(x)+'\n')

        f.close()

    def create_widgets(self):
     
        self.label1 = Label(self, text="N° du test")
        self.label1.grid(row=0, column=0)

        self.numerotest = Entry(self, bd =5)
        self.numerotest.grid(row=0, column=1)
        self.numerotest.delete(0,END)
        self.numerotest.insert(0,"Test n° 111");

        self.label2 = Label(self, text="Date du test")
        self.label2.grid(row=1, column=0)
        # remplir la date avec la date du jour
        aujourdhui=datetime.now()

        self.datetest = Entry(self, bd =5)
        self.datetest.grid(row=1, column=1)
        self.datetest.delete(0,END)
        self.datetest.insert(0, aujourdhui.strftime("%Y-%m-%d-%Hh%M"))
        self.filename=self.numerotest.get()+"-"+aujourdhui.strftime("%Y-%m-%d-%Hh%M")
        
        self.run = tk.Button(self, text="Run",command=self.runTest)
        self.run.grid(row=2, column=0)

        self.save = tk.Button(self, text="Save",command=self.saveTest)
        self.save.grid(row=2, column=1)
        
        self.quit = tk.Button(self, text="QUIT", fg="red",command = self.master.destroy)
        self.quit.grid(row=3, column=1)



root = tk.Tk()
app = Application(master=root)
app.mainloop()
