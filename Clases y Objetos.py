# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
class myCelular():
    # Constructor
    def __init__(self, marca_entra, modelo_entra, precio_entra):
        # Atributos
        self.marca_dentro = marca_entra
        self.modelo_dentro = modelo_entra
        self.precio_dentro = precio_entra

    # Metodo.
    def myMarca(self):
        print(f'imprimiendo el celular: {self.marca}')

    # Metodo.
    def myModelo(self):
        print(f'imprimiendo el celular: {self.modelo}')

    # Metodo.
    def myPrecio(self):
        print(f'imprimiendo el celular: {self.precio}')


# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# Creamos el objeto = pasamos los atributos de instancia
objeto1 = myCelular("sansumg", "jp 200", 1500000)

# llamando funcion
objeto1.myMarca()


# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# Crear un objeto de la clase


class ClaseBase:
    def metodo_base(self):
        print("Método de la clase base")


class ClaseDerivada(ClaseBase):
    def metodo_derivado(self):
        print("Método de la clase derivada")

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# objeto_derivado = ClaseDerivada()
# objeto_derivado.metodo_base()
# objeto_derivado.metodo_derivado()

# print(objeto1.marca)
# print(objeto1.modelo)
# print(objeto1.precio)

# ClaseDerivada.metodo_derivado
