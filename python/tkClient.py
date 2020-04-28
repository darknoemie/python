import tkinter as tk
from tkinter import messagebox
from tkinter import Label
from tkinter import Entry
from tkinter import Text
from tkinter import Listbox
from tkinter import Scrollbar
import postgres.ClientDAO as ClientDAO

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.ids=list()
        self.pack()
        self.fields = ['id','mnemo','raison','adresse1','adresse2','codeinsee']
        self.create_widgets()
        self.loaddata()


    def create_widgets(self):
        
        for f in self.fields:
            str =f
        
        label1 = Label(self, text="Mnemo")
        label1.grid(row=0, column=0)

        self.mnemo = Entry(self, bd =5)
        self.mnemo.grid(row=0, column=1)

        label2 = Label(self, text="Raison")
        label2.grid(row=1, column=0)

        self.raison = Entry(self, bd =5)
        self.raison.grid(row=1, column=1)
                
        label3 = Label(self, text="Adresse")
        label3.grid(row=2, column=0)

        self.adresse1 = Entry(self, bd =5)
        self.adresse1.grid(row=2, column=1)
           
        label4 = Label(self, text="")
        label4.grid(row=3, column=0)

        self.adresse2 = Entry(self, bd =5)
        self.adresse2.grid(row=3, column=1)     
     
        label5 = Label(self, text="Code insee")
        label5.grid(row=4, column=0)

        self.codeinsee = Entry(self, bd =5)
        self.codeinsee.grid(row=4, column=1)    
        self.listbox = Listbox(self)
        self.scrollbar = Scrollbar(self,command=self.listbox.yview)
        self.listbox.config( yscrollcommand = self.scrollbar.set)
        self.listbox.bind('<<ListboxSelect>>', self.listboxCallback)
        self.scrollbar.grid(row=0, column=3,rowspan=5,sticky='ns')
        self.listbox.grid(row=0, column=2,rowspan=5)
        
        self.panelBtn = tk.PanedWindow(self)
        self.panelBtn.grid(row=6,column=0,columnspan=3)
        
        self.btnInsert = tk.Button(self.panelBtn)
        self.btnInsert["text"] = "Insert"
        self.btnInsert["command"] = self.insert
        self.panelBtn.add(self.btnInsert)
        
        self.btnUpdate = tk.Button(self.panelBtn)
        self.btnUpdate["text"] = "Update"
        self.btnUpdate["command"] = self.update
        self.panelBtn.add(self.btnUpdate)
 
        self.quit = tk.Button(self.panelBtn, text="QUIT", fg="grey", command=self.master.destroy)
        self.panelBtn.add(self.quit)


    def insert(self):
        dao=ClientDAO.ClientDAO()
        entity={}
        entity['mnemo']=self.mnemo.get()
        entity['raison']=self.raison.get()
        entity['adresse1']=self.adresse1.get()
        entity['adresse2']=self.adresse2.get()
        entity['codeinsee']=self.codeinsee.get()
        lastid=dao.save(entity)
        
    def update(self):
        dao=ClientDAO.ClientDAO()
        entity={}
        entity['id']=self.currentId
        entity['mnemo']=self.mnemo.get()
        entity['raison']=self.raison.get()
        entity['adresse1']=self.adresse1.get()
        entity['adresse2']=self.adresse2.get()
        if self.codeinsee.get():
            entity['codeinsee']=self.codeinsee.get()
        #print("tkClient.update: entity={}".format(entity))
        lastid=dao.update(entity)
        
    def loaddata(self):    
        dao=ClientDAO.ClientDAO()
        rows = dao.getAll()
        for row in rows:
            # On stocke les id dans un tableau
            self.ids.append(row['id'])
            #print("id={0},raison={1}".format(row['id'],row['raison']))
            str=row['raison']
            self.listbox.insert(tk.END,str)
            
     
    def listboxCallback(self,event):
        try:
            w = event.widget
            index = int(w.curselection()[0])
            #print("index={0},id={1}".format(index,self.ids[index]))
            value = w.get(index)
            curIndex = event.widget.nearest(event.y)
            dao=ClientDAO.ClientDAO()
            self.currentId=self.ids[index]
            #print("currentId={0}".format(self.currentId))
            row = dao.getById(self.currentId)
            #print("row={}".format(row))
            self.mnemo.delete(0, tk.END)
            self.raison.delete(0, tk.END)
            self.adresse1.delete(0, tk.END)
            self.adresse2.delete(0, tk.END)
            self.codeinsee.delete(0, tk.END)
            
            if row['mnemo']:
                self.mnemo.insert(0, row['mnemo'])
            if row['raison']:
                self.raison.insert(0, row['raison'])
            if row['adresse1']:
                self.adresse1.insert(0, row['adresse1'])
            if row['adresse2']:
                self.adresse2.insert(0, row['adresse2'])
            if row['codeinsee']:
                self.codeinsee.insert(0, row['codeinsee'])
        except IndexError as msg:
            print("la liste est vide")   

root = tk.Tk()
app = Application(master=root)
app.mainloop()