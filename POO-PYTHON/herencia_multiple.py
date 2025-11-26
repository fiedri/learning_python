class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}."
 
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad artística es {self.habilidad}."

class EstudianteArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, carrera, universidad):
        # se hace referencia directa a las clases padres
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.carrera = carrera
        self.universidad = universidad

    def mostrar_habilidad(self):
        return "No tengo una habilidad artística"
    def presentarse(self):
        saludo = super().saludar()
        # si uso super() accedo al metodo en la clase padre sino accederia al metodo sobreescrito en esta clase
        return f"{saludo} Soy estudiante de {self.carrera} en {self.universidad} y {self.mostrar_habilidad()}."
    
maria = EstudianteArtista("María", 22, "colombiana", "pintura", "Arquitectura", "Universidad Nacional")
print(maria.presentarse())

herencia = issubclass(EstudianteArtista, Persona)
print(f"¿EstudianteArtista es subclase de Persona? {herencia}")

es_instancia = isinstance(maria, EstudianteArtista)
print(f"¿María es instancia de EstudianteArtista? {es_instancia}")