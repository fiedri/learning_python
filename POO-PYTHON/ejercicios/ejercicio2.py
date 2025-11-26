class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"Datos Personales - Nombre: {self.nombre}, Edad: {self.edad}"
    
class Estuadiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_grado(self):
        return f"Carrera: {self.carrera}"
    
estudiante1 = Estuadiante("Ana", 20, "Ingeniería")
print(estudiante1.mostrar_info())
print(estudiante1.mostrar_grado())
