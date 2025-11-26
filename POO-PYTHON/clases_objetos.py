# Se usa la palabra reservada 'class', y con el formato pascalcase
class Celular:
    # atributos estaticos. Son fijos para todos los objetos de la clase
    propiedad1= 'valor1'
    propiedad2 = 'valor2  '
    #self hace referencia al objeto actual de la clase, similar a 'this' en otros lenguajes

    # El método __init__ es el constructor de la clase
    def __init__(self, marca, modelo, color, almacenamiento):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento
        self.encendido = False

    # los metodos son funciones dentro de la clase, utilizan 'self' como primer parametro para autoreferenciarse
    # Método para encender el celular
    def encender_celular(self):
        if not self.encendido:
            self.encendido = True
            return "El celular está encendido."
        else:
            return "El celular ya está encendido."

    # Método para apagar el celular
    def apagar_celular(self):
        if self.encendido:
            self.encendido = False
            return "El celular está apagado."
        else:
            return "El celular ya está apagado."

    # Método para mostrar la información del celular
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Almacenamiento: {self.almacenamiento}GB"
    
# Crear un objeto de la clase Celular, Instanciación
mi_celular = Celular("Samsung", "Galaxy S21", "Negro", 128)
print(mi_celular.mostrar_info())
print(mi_celular.encender_celular())
print(mi_celular.encender_celular())