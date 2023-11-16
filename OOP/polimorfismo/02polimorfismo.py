# objetos con forma
# forma hereda a cuadrado y circulo
# cuadrados tienen lados y lso circulos radios
# todos tienen metoodo calcular area.

class Forma:
    def calcular_area(self):
        print("Class Forma metho0")

class Cuadrado():
    def __init__(self, lado):
        self.lado = lado
        print("Class Cuadrado metho1")
    
    def calcular_area(self):
        print("Class Cuadrado metho2")
        return self.lado ** 2
        
class Circulo():
    def __init__(self, radio):
        self.radio = radio
        print("Class Circulo metho3")
    
    def calcular_area(self):
        print("Class Circulo metho4")
        return 3.14 * self.radio ** 2
        
# SEGUNDA PARTE
def imprimir_area(forma):
    print("Área:", forma.calcular_area())
    print("area impresa")

cuadrado = Cuadrado(5)
circulo = Circulo(3)
imprimir_area(cuadrado)  # Imprime el área del cuadrado
imprimir_area(circulo)   # Imprime el área del círculo
