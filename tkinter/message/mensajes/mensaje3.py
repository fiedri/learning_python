import tkinter as tk
from tkinter import messagebox, filedialog

def seleccionar_archivo():
    # Abrir el explorador de archivos y guardar la ruta seleccionada
    ruta = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    # Si el usuario seleccionó algo (no canceló)
    if ruta:
        messagebox.showinfo("Archivo Seleccionado", f"Has elegido:\n{ruta}")
    else:
        messagebox.showwarning("Cancelado", "No seleccionaste ningún archivo.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Selector de Archivos Linux")
ventana.geometry("400x200")

label = tk.Label(ventana, text="Presiona el botón para buscar un archivo:", pady=20)
label.pack()

# Botón que dispara el explorador de archivos
boton_buscar = tk.Button(ventana, text="Buscar Archivo...", command=seleccionar_archivo, bg="orange")
boton_buscar.pack()

ventana.mainloop()