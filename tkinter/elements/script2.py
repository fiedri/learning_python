import tkinter as tk
from tkinter import messagebox

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Este es el nombre de la ventana")
ventana.geometry("500x800")

# 1. LABEL: Un título descriptivo
titulo = tk.Label(ventana, text="Esto es un titulo", font=("Arial", 14, "bold"), fg="blue")
titulo.pack(pady=10)

# 2. MESSAGE: Para textos largos explicativos
instrucciones = tk.Message(ventana, text="Esto es un texto que puede abarcar varias lineas, en pocas palabras un parrafo", width=400)
instrucciones.pack(pady=5)

# 3. FRAME: Un contenedor para organizar otros widgets
marco_entrada = tk.Frame(ventana, bd=2, relief="groove", padx=10, pady=10)
marco_entrada.pack(pady=10, fill="x", padx=20)

# 4. ENTRY: Campo para texto cort
tk.Label(marco_entrada, text="Esto es otro texto en un label").pack()
entrada_objetivo = tk.Entry(marco_entrada, width=40)
entrada_objetivo.pack()

# 5. CHECKBUTTON
var_check = tk.IntVar()
check_disciplina = tk.Checkbutton(ventana, text="Esto es un boton de check", variable=var_check)
check_disciplina.pack(pady=5)

# 6. RADIOBUTTONS: Seleccionar una opción entre varias
tk.Label(ventana, text="Selecciona una opción:").pack()
var_radio = tk.StringVar(value="Medio")
tk.Radiobutton(ventana, text="Bajo (En riesgo)", variable=var_radio, value="Bajo").pack()
tk.Radiobutton(ventana, text="Medio (Estable)", variable=var_radio, value="Medio").pack()
tk.Radiobutton(ventana, text="Alto (Modo Monje)", variable=var_radio, value="Alto").pack()

# 7. SCALE: Un deslizador numérico (Ej: Nivel de energía)
tk.Label(ventana, text="Nivel de energía").pack()
deslizador = tk.Scale(ventana, from_=0, to=100, orient="horizontal")
deslizador.pack(fill="x", padx=50)

# 8. SPINBOX: Selección numérica con flechas
tk.Label(ventana, text="Seleccion numerica").pack()
selector_horas = tk.Spinbox(ventana, from_=0, to=24)
selector_horas.pack()

# 9. LISTBOX y SCROLLBAR: Una lista con barra de desplazamiento
tk.Label(ventana, text="Caja de lista y con scrollbar").pack(pady=5)
marco_lista = tk.Frame(ventana)
marco_lista.pack()

scrollbar = tk.Scrollbar(marco_lista)
scrollbar.pack(side="right", fill="y")

lista_items = tk.Listbox(marco_lista, yscrollcommand=scrollbar.set, height=4)
for item in ["Python", "Tkinter", "Estructura de Datos", "Backend", "Frontend", "Cloud"]:
    lista_items.insert("end", item)
lista_items.pack(side="left")
scrollbar.config(command=lista_items.yview)

# 10. TEXT: Área para notas largas
tk.Label(ventana, text="Notas largas").pack(pady=5)
area_texto = tk.Text(ventana, height=5, width=40)
area_texto.pack()

# 11. CANVAS: Para dibujos o formas geométricas
lienzo = tk.Canvas(ventana, width=200, height=40, bg="white")
lienzo.pack(pady=10)
lienzo.create_rectangle(0, 0, 200, 40, fill="#e0e0e0")
lienzo.create_text(100, 20, text="PROGRESO VISUAL", fill="black")

# 12. BUTTON: El disparador de la lógica
def registrar_datos():
    objetivo = entrada_objetivo.get()
    nivel = var_radio.get()
    if var_check.get() == 1:
        messagebox.showinfo("Éxito", f"Objetivo '{objetivo}' guardado.")
    else:
        messagebox.showwarning("Atención", "Recuerda que el dominio propio es la base de tu éxito.")

boton_accion = tk.Button(ventana, text="REGISTRAR AVANCE", command=registrar_datos, bg="#4CAF50", fg="white")
boton_accion.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()