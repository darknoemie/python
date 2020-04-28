import tkinter as tk

mainFrame = tk.Tk()

canvas = tk.Canvas(mainFrame, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
angle = 345
arc = canvas.create_arc(coord, start=0, extent=angle, fill="lightblue")

canvas.pack()
mainFrame.mainloop()
