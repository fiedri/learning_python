# una clase abstrata es una clase que no se instancia, pero sirve para crear
# otras clases a partir de esa como si fuera una plantilla


from abc import ABC, abstractclassmethod

# clase abstracta
# una clase que existe solo para obligar a otras a seguir ciertas reglas
# no puede ser instanciada
class Persona:
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad =actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"hola me llamo {self.nombre} y tengo  {self.edad}")