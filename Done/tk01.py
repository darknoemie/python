import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.clickMe = tk.Button(self)
        self.clickMe["text"] = "Hello Wonderfull World\n(click me)"
        self.clickMe["command"] = self.dit_bonjour
        self.clickMe.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def dit_bonjour(self):
        print("Bonjour, everybody!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
