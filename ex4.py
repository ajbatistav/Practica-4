class personaje:
    def __init__(self, MoverArriba, MoverAbajo, MoverDerecha, MoverIzquierda):
        self.arriba = MoverArriba
        self.abajo = MoverAbajo
        self.derecha = MoverDerecha
        self.izquierda = MoverIzquierda
    
    class Mario(personaje):
        pass
    class koopa(personaje):
        pass
