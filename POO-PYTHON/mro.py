# el mro (method resolution order) define el orden en que se buscan los metodos en la jerarquia de clases
class A:
    def hablar(self):
        return "Hola desde la clase a"
    
class B(A):
    def hablar(self):
        return "Hola desde la clase B"

class C(A):
    def hablar(self):
        return "Hola desde la clase C"

class D(B, C):
    # el mro toma el primer metodo que encuentra en el orden de herencia, si no lo encuentra en la primera clase, busca en la segunda, y asi sucesivamente
    # D> B || C > A
    """El mro busca en b luego en a, si no lo encuentra en ninguna de las 2 busca en c y luego en a"""
    def Saludar(self):
        return super().hablar()
    
obj = D()
print(obj.Saludar())

print(A.hablar(obj))
print(D.mro())