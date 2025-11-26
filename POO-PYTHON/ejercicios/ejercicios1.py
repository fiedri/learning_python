class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        materia= input("Ingrese la materia que va a estudiar: ")
        return f"{self.nombre} está estudiando {materia}."
    
# Crear un objeto de la clase Estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: "))
grado_estudiante = input("Ingrese el grado del estudiante: ")
mi_estudiante = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante)

print(mi_estudiante.estudiar())
print(mi_estudiante.estudiar())