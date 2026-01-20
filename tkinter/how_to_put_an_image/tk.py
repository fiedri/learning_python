from tkinter import *
import os
root = Tk()

root.title("Imagen en tk")
root.geometry("600x400")

img_path = os.path.join(os.path.dirname(__file__), 'foto.gif')

imagen = PhotoImage(file=img_path)

label = Label(image=imagen)
label.pack()

root.mainloop()