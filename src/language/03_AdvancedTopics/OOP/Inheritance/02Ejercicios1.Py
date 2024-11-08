# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
class Estudiante():
    # Constructor
    def __init__(self, nombre, edad, grado):
        # Atributos
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Metodo.
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#


# Imprimir peticion
nombre = input("Por, favor ingrese su nombre.")
edad = int(input("Por, favor ingrese su edad."))
grado = input("Por, favor ingrese su grado.")

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
        Datos Del Estudiante-->
        nombre: {nombre}
        edad: {edad}
        grado: {grado}
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
        exit
