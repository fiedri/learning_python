from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Editor de notas")
root.geometry("400x400")

barra_menu = Menu(root)
root.config(menu=barra_menu)

menu_archivo = Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")

root.mainloop()