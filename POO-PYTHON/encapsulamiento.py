class MiClase:
    def __init__(self):
        # atributo privado _
        # es solo una convencion
        self._atributo_privado = "valor"
        # atributo muy privado __
        # muy privado no es accedible
        self.__atributo_muy_privado = "valor2"

    ## metodos privados
    # def _saludar():
    #     print("hola")
    # def __hablar():
    #     print("HOla, como estas")
    ## getters y setters
    @property # le dice que es un getter
    def atributo(self):
        return self.__atributo_muy_privado
    
    @atributo.setter # le dice que es un setter tiene el nombre de la funcion
    def atributo(self, nuevo_valor):
        self.__atributo_muy_privado = nuevo_valor

    @atributo.deleter
    def atributo(self):
        del self.__atributo_muy_privado

objecto = MiClase()
print(objecto.atributo)
objecto.atributo = "otro valor"
print(objecto.atributo)
del objecto.atributo

# print(objecto.atributo) da error porque ya no existe