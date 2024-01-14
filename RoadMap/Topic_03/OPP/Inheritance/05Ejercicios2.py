class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def printPersonaAll(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")

# Si usamos la func super no se debe pasar self
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def printEstudianteAll(self):
        print(f"grado: {self.grado}")


estu1 = Estudiante("carlos", "27", "sexto")

estu1.printPersonaAll()
estu1.printEstudianteAll()
