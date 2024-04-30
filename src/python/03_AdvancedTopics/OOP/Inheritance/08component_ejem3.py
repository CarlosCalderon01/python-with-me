

class Comer:
    def comer(self):
        print("Comiendo")


class Dormir:
    def dormir(self):
        print("Durmiendo")


class Animal:
    # creo una variale almacenadora "comportamientos"
    def __init__(self):
        self.comportamientos = []

    # agrega el comportamiento al almacen
    def agregar_comportamiento(self, comportamiento):
        self.comportamientos.append(comportamiento)

    #ejecuta el comportamiento para cada comportamiento almacenado
    def realizar_comportamientos(self):
        for comportamiento in self.comportamientos:
            comportamiento()


tigre = Animal()

tigre.agregar_comportamiento(Comer().comer)
tigre.agregar_comportamiento(Dormir().dormir)

tigre.realizar_comportamientos()

# instancio objeto class Animal
# a travez de las funciones d ela instancia paso las funciones de los comportamientos.