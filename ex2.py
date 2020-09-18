class estudiante:
    def __init__(self,nombre,curso):
        self.nombre = str(nombre)
        self.curso = str(curso)


    def promedio(self):
        prod = 0
        while prod <= 100:
            n_1 = float(input("Introduzca la primera calificacion: "))
            n_2 = float(input("Introduzca la segunda calificacion: "))
            n_3 = float(input("Introduzca la tercera calificacion: "))
            n_4 = float(input("Introduzca la cuarta calificacion: "))
            prod = float((n_1 + n_2 + n_3 + n_4) / 4)
            if prod <= 100:
                print(f"Su promedio es {prod} ")
                salida = int(input("Volver a promediar (1), Salir(2) "))
                if salida == 1:
                    prod = 0
                elif salida == 2:
                    prod = 101        
            else:
                print("Valores de calificaciones no válidos.")    
                prod = 0


prueba= estudiante(4,3)
prueba.promedio()
