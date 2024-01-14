class Animal():
    def comer(self):
        print("class Animal method comer")


class Mamifero(Animal):
    def amamantar(self):
        print("class Mamifero method amamantar")


class Ave(Animal):
    def volar(self):
        print("class Ave method volar")


class Murcielago(Mamifero, Ave):
    pass


murcielago1 = Murcielago()

murcielago1.comer()
murcielago1.amamantar()
murcielago1.volar()
