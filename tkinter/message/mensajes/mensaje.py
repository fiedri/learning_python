from tkinter import *
from tkinter import messagebox

def saludar():
    messagebox.showinfo("Mensaje", "¡Has presionado el botón!")


ventana = Tk()
ventana.title("Mi Aplicación")
ventana.geometry("300x200") 

etiqueta = Label(ventana, text="Haz clic para ver el mensaje:", pady=20)
etiqueta.pack()

boton = Button(ventana, text="Mostrar Alerta", command=saludar, bg="lightblue")
boton.pack(pady=10)

ventana.mainloop()