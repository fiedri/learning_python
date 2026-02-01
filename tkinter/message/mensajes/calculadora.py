from tkinter import *
from tkinter import messagebox


def calcular():
    numero1=n1.get()
    numero2=n2.get()
    op=operacion.get()
    result=eval(f"{numero1}{op}{numero2}")
    if not result: result=0
    messagebox.showinfo("Resulado", result)

ventana = Tk()
ventana.title("Mi App Interactiva")
ventana.geometry("350x250")
Label(ventana, text="Numero 1").pack()
n1= Entry(ventana)
n1.pack()
Label(ventana, text="Operacion").pack()
operacion=Entry(ventana)
operacion.pack()
Label(ventana, text="Numero 2").pack()
n2= Entry(ventana)
n2.pack()
btn= Button( text="calcular", command=calcular, bg="#4CAF50", fg="white")
btn.pack()
ventana.mainloop()