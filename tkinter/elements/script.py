from tkinter import *

root = Tk()
# nombre de la ventana
root.title("Simple Tkinter Window")
# Tamaño de la ventana
root.geometry("300x600")

# Texto o imagenes
label = Label(root, text="Hello, Tkinter!")
label.pack(pady=20) # pady = padding vertical

# Boton
btn = Button(root, text="Click Me", command=lambda: print("Button Clicked!"))
btn.pack(pady=10)

# Entrada de texto
input = Entry(root)
input.pack(pady=10)

# Texto multilinea
text = Text(root, height=15, width=20)
text.pack(pady=10)


# mensaje
message = Message(root, text="This is a simple message widget.", width=200)
message.pack(pady=10)
root.mainloop()