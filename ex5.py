class carro:
    def __init__(self, galones):
       self.cantidadCombustible = galones
       self.encendido = False

    def encender(self):
        if self.encendido == False and self.cantidadCombustible > 0 :
            self.encendido = True
            print("El vehiculo avanzo")
            self.cantidadCombustible -= 1
            print(self.cantidadCombustible)

    

civic = carro(8)
civic.encender()
civic.encender()