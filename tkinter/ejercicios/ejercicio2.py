from tkinter import *
from tkinter import messagebox

def add_task(event=None):
    task = Entry_task.get()
    if task.strip(): # .strip() evita que agreguen tareas vacías con puros espacios
        listbox_task.insert(END, task)
        Entry_task.delete(0, END)
    else:
        messagebox.showwarning("Error", "No puedes agregar una tarea vacía.")

def clear_tasks():
    listbox_task.delete(0, END)

def delete_task():
    selected_task_index = listbox_task.curselection()
    if selected_task_index:
        listbox_task.delete(selected_task_index)
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

root = Tk()
root.title("Lista de tareas")
root.geometry("400x400")
Label(root, text="Nueva Tarea:").pack(pady=5)
Entry_task = Entry(root, width=30)
Entry_task.pack(pady=10)

# Esto vincula la tecla Enter a la función add_task
Entry_task.bind('<Return>', add_task)

btn_add = Button(root, text="Agregar (Enter)", command=add_task, bg="#e1e1e1")

btn_delete = Button(root, text="Eliminar tarea", command=delete_task)
btn_clear = Button(root, text="Limpiar lista", command=clear_tasks)

btn_add.pack(pady=5)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox_task = Listbox(root, height=10, width=50, yscrollcommand=scrollbar.set)
listbox_task.pack(pady=10)
scrollbar.config(command=listbox_task.yview)
btn_delete.pack(pady=5)
btn_clear.pack(pady=5)
root.mainloop()