# son metodos que inician con guiones bajos y terminan con guiones bajos
class Persona:
    # __init__ es un metodo especial
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # devuelve una representacion de la clase en string
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

persona = Persona("Friedrich", 17)

print(persona)# imprime lo que devuelve __str__