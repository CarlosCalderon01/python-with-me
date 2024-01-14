# Probando jerarquia de herencias MRO

# abstract: MRO - Méthod Resolution Order, metodo que indica la jerarquia.
# primero son las clases de izquierda a derecha, y antes de avanzar a la siguiente.
# ella recorre todas las super clases hasta el final.

class A():
    def hablar(self):
        print("Hola Desde Clase A")

class B(A):
    def hablar(self):
        print("Hola Desde Clase B")

class C(A):
    def hablar(self):
        print("Hola Desde Clase C")

class D(B, C):
    def hablar(self): 
        print("Hola Desde Clase D")

class E():
    def hablar(self):
        print("Hola Desde Clase E")

