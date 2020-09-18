class aritmetica:
    def __init__(self):
       pass
    
    def sumar(self):
        a_s = int(input("Introduzca el primer valor: "))
        b_s = int(input("Introduzca el segundo valor: "))
        resultado_suma = a_s + b_s
        print(f"{a_s} + {b_s} = {resultado_suma} ")
    
    def restar(self):
        a_s = int(input("Introduzca el primer valor: "))
        b_s = int(input("Introduzca el segundo valor: "))
        resultado_suma = a_s - b_s
        print(f"{a_s} - {b_s} = {resultado_suma} ")
    
    def multiplicacion(self):
        a_s = int(input("Introduzca el primer valor: "))
        b_s = int(input("Introduzca el segundo valor: "))
        resultado_suma = a_s * b_s
        print(f"{a_s} X {b_s} = {resultado_suma} ")        
    
    def division(self):
        a_s = int(input("Introduzca el primer valor: "))
        b_s = int(input("Introduzca el segundo valor: "))
        resultado_suma = a_s / b_s
        print(f"{a_s} / {b_s} = {resultado_suma} ")        




op = aritmetica()
op.sumar()
op.restar()
op.multiplicacion()
op.division()






