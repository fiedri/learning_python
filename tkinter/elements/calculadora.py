import tkinter as tk
from tkinter import messagebox

# --- FUNCIONES DE LÓGICA ---
def click_boton(valor):
    # Inserta el valor del botón en la pantalla
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, str(actual) + str(valor))

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

def calcular_resultado():
    try:
        # eval() evalúa la cadena de texto como una operación matemática
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except Exception:
        messagebox.showerror("Error", "Entrada inválida")
        limpiar_pantalla()

# --- CONFIGURACIÓN DE LA VENTANA ---
ventana = tk.Tk()
ventana.title("Calculadora de Dominio")
ventana.configure(bg="#1e1e1e") # Color oscuro de fondo

# --- PANTALLA (ENTRY) ---
# Usamos justify='right' para que los números salgan a la derecha como en una calculadora real
pantalla = tk.Entry(ventana, font=("Courier New", 20), borderwidth=5, relief="flat", justify="right", bg="#2d2d2d", fg="#ffffff")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# --- DEFINICIÓN DE BOTONES ---
# Estilo común para los botones
estilo_botones = {"font": ("Arial", 14), "bg": "#333333", "fg": "white", "padx": 20, "pady": 20, "relief": "flat"}
estilo_operadores = {"font": ("Arial", 14), "bg": "#ff9500", "fg": "white", "padx": 20, "pady": 20, "relief": "flat"}

# Lista de botones (Texto, Fila, Columna)
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Crear botones dinámicamente
for (texto, fila, columna) in botones:
    if texto == '=':
        btn = tk.Button(ventana, text=texto, **estilo_operadores, command=calcular_resultado)
    elif texto in ['/', '*', '-', '+']:
        btn = tk.Button(ventana, text=texto, **estilo_operadores, command=lambda t=texto: click_boton(t))
    else:
        btn = tk.Button(ventana, text=texto, **estilo_botones, command=lambda t=texto: click_boton(t))
    
    btn.grid(row=fila, column=columna, sticky="nsew", padx=2, pady=2)

# Botón para limpiar (ocupa todo el ancho abajo)
boton_borrar = tk.Button(ventana, text="LIMPIAR MENTE (C)", bg="#d9534f", fg="white", font=("Arial", 12, "bold"), command=limpiar_pantalla)
boton_borrar.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=5)

# Ajustar el peso de las columnas para que se expandan uniformemente
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()