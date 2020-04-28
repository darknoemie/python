import tkinter as tk
from tkinter import Checkbutton
from tkinter import messagebox

mainFrame = tk.Tk()
""" Callback """


def checkboxCallBack():
    str = "Securisation:{0}\nAccélération:{1},\nTerminée:{2}".format(checkVar1.get(), checkVar2.get(), checkVar3.get())
    messagebox.showinfo("Résultat", str)


""" IntVar() est un wrapper pour des valeurs entières """
checkVar1 = tk.IntVar()
checkVar2 = tk.IntVar()
checkVar3 = tk.IntVar()
chkbtn1 = Checkbutton(mainFrame, text="Sécurisation", variable=checkVar1, \
                      onvalue=1, offvalue=0, height=2, \
                      width=20, command=checkboxCallBack)
chkbtn2 = Checkbutton(mainFrame, text="Accélération", variable=checkVar2, \
                      onvalue=1, offvalue=0, height=2, \
                      width=20, command=checkboxCallBack)
chkbtn3 = Checkbutton(mainFrame, text="Terminée", variable=checkVar3, \
                      onvalue=1, offvalue=0, height=2, \
                      width=20, command=checkboxCallBack)
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()
mainFrame.mainloop()
