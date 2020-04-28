import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import END
from _datetime import datetime
from random import random

import psycopg2

import numpy
from matplotlib import pyplot

"""
TP2: TK
== Etape 2 ==
En partant du TP1-tk.py, on enregistrera les valeurs dans une base de données PostgreSQL.

Créer les tables pour stocker les tests et les valeurs
- le nom du test
- la date du test 
- les valeurs

-- La table des tests
create sequence seq_test
start with 1
increment 1;

create table test (
id int8 primary key default nextval('seq_test'),
nom varchar null,
datetest timestamp null
);

-- La table des valeurs
create sequence seq_valeur
start with 1
increment 1;

create table valeur (
id int8 primary key default nextval('seq_valeur'),
idTest int8,
valeur float8 null
);

"""

class Application(tk.Frame):
    def __init__(self, master=None, maxvalues=10):
        super().__init__(master)
        self.master = master
        self.maxvalues=maxvalues
        self.pack()
        self.create_widgets()
        """ On récupère dans cnx un objet connexion """
        self.cnx = psycopg2.connect(host="localhost",database="cours", user="postgres", password="secret")

       
    def generate_values(self):
        self.listofvalues = []
        for i in range(self.maxvalues):
            x = int(random() * 1000)    
            print (x) 
            self.listofvalues.append(x)
            
    def runTest(self):
        s ="Test {0} , lancé le {1}".format(self.numerotest.get(),self.datetest.get())
        print(s)  
        self.generate_values()  
        
    def runShow(self):
        x = numpy.arange(self.maxvalues)
        #y = numpy.array([5,3,4,2,7,5,4,6,3,2])
        y = numpy.array(self.listofvalues)

        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        ax.set_ylim(0,1000)
        pyplot.plot(x,y)
        for i,j in zip(x,y):
            ax.annotate(str(j),xy=(i,j))
        # Afficher un second graphique
        x2=range(10) 
        y2 = numpy.array([500,300,400,200,700,500,400,600,300,200])
        pyplot.plot(x2,y2)
        
        pyplot.show()    
        
    def saveTest(self):
        """ Ajouter un test """
        sql="insert into test (nom) values (%s)"
        cursor = self.cnx.cursor()
        listValues=[]
        listValues.append(self.numerotest.get())
        
        cursor.execute(sql,listValues)
        self.cnx.commit()
        cursor.close()
        """ Récupère le dernier identifiant """
        sql="SELECT currval('seq_test')"
        cursor = self.cnx.cursor()
        cursor.execute(sql)
        """ Lit la valeur du dernier identifiant"""
        row = cursor.fetchone()
        lastid=row[0]
        print(lastid)
        cursor.close() 
        """ Insere les valeurs """
        sql="insert into valeur (idtest,valeur) values (%s,%s)"
        cursor = self.cnx.cursor()
        for x in self.listofvalues:
            listOfParams=[]
            listOfParams.append(lastid)
            listOfParams.append(x)
            cursor.execute(sql,listOfParams)
        self.cnx.commit()
        cursor.close()    


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
        
        self.run = tk.Button(self, text="Show",command=self.runShow)
        self.run.grid(row=3, column=0)
        
        self.quit = tk.Button(self, text="QUIT", fg="red",command = self.master.destroy)
        self.quit.grid(row=3, column=1)



root = tk.Tk()
app = Application(master=root,maxvalues=50)
app.mainloop()
db
