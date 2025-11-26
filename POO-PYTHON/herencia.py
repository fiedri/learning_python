class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}."
    
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo: str, salario: float):
        #atributos heredados
        super().__init__(nombre, edad, nacionalidad)
        #atributos propios
        self.trabajo = trabajo
        self.salario = salario
        
    def presumir(self):
        print(f"Trabajo como {self.trabajo} y gano {self.salario}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, carrera: str, universidad: str):
        #atributos heredados
        super().__init__(nombre, edad, nacionalidad)
        #atributos propios
        self.carrera = carrera
        self.universidad = universidad
        
    def estudiar(self):
        print(f"Estoy estudiando {self.carrera} en {self.universidad}.")

## herencia multiple
class PersonaNormal(Empleado, Estudiante):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario, carrera, universidad):
        Empleado.__init__(self, nombre, edad, nacionalidad, trabajo, salario)
        Estudiante.__init__(self, nombre, edad, nacionalidad, carrera, universidad)

roberto = Empleado("Roberto", 30, "mexicano", "Ingeniero", 50000)

print(roberto.saludar())
roberto.presumir()