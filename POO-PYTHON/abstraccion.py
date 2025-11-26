class Auto:
    def __init__(self):
        self._estado = 'apagado'
    
    def encender(self):
        print('auto encendido')
        self._estado = 'encendido'
    
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print("conduciendo auto")    

mi_carro = Auto()


mi_carro.conducir()