from tkinter import *
from tkinter import messagebox

def mostrar_saludo():
    
    nombre = caja.get()
    
    if nombre.strip() == "":
        messagebox.showwarning("Atención", "Por favor, escribe tu nombre primero.")
    else:
        messagebox.showinfo("Mensaje:", nombre)


ventana = Tk()
ventana.title("Mi App Interactiva")
ventana.geometry("350x250")


mensaje = Label(text="Escribe tu nombre:", font=("Arial", 12))
mensaje.pack(pady=10)

caja = Entry(font=("Arial", 12))
caja.pack(pady=5)

boton_saludar = Button( text="¡Salúdame!", command=mostrar_saludo, bg="#4CAF50", fg="white")
boton_saludar.pack(pady=20)

ventana.mainloop()