from tkinter import *
from tkinter import messagebox

def calcular_propina():
    try:
        cuenta = float(entrada_cuenta.get())
        propina = float(entrada_propina.get())
        if not cuenta or not propina:
            messagebox.showwarning("Error", "Por favor, ingresa ambos valores.")
            return
        propina = cuenta * (propina / 100)
        messagebox.showinfo("Resultado", f"La propina sugerida es: ${propina}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
        return


ventana = Tk()
ventana.title("Calculadora de propinas")
ventana.geometry("400x600")

Label(ventana, text="Calculadora de Propinas", font=("Arial", 16, "bold")).pack(pady=10)
Label(ventana, text="Cuenta Total ($):").pack(pady=5)
entrada_cuenta = Entry(ventana, width=30)
entrada_cuenta.pack()

Label(ventana, text="Porcentaje de Propina:").pack(pady=5)
entrada_propina = Entry(ventana, width=30)
entrada_propina.pack()

Button(ventana, text="Calcular Propina", command=calcular_propina).pack(pady=20)


ventana.mainloop()