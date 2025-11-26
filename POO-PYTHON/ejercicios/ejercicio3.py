class Animal:
    def comer(self):
        return "El animal está comiendo."
class Mamifero(Animal):
    def amamantar(self):
        return "El mamífero está amamantando a sus crías."

class Ave(Animal):
    def volar(self):
        return "El ave está volando."
    
class Murcielago(Mamifero, Ave):
    pass

murcielago1 = Murcielago()
print(murcielago1.comer())
print(Murcielago.mro())