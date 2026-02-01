from tkinter import *


def get_data():
    data1= caja1.get()
    data2= caja2.get()
   
    message1.config(text=f"Usuario: {data1}")
    message2.config(text=f"Correo: {data2}")
    caja1.delete(0, END)
    caja2.delete(0, END)

root = Tk()
    
root.title("Titulo de ventana")
root.geometry("600x400")

Label(root, text="Usuario").pack()
caja1 = Entry(root)
caja1.pack(pady=20)
Label(root, text="correo").pack()
caja2 = Entry(root)
caja2.pack(pady=20)


btn = Button(root, text="Haz click", command=get_data)
btn.pack()
message1 = Label(root, text="", width=400)
message1.pack()
message2 = Label(root, text="", width=400)
message2.pack()

root.mainloop()