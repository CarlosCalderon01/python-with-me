# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
class myUsuario():
    def __init__(self, nombre, apellido, edad, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pais = pais

    # print data user.
    def printSoloUsuario(self):
        print(f"""
            Datos Solo Usuario-->
            nombre: {self.nombre}
            apellido: {self.apellido}
            edad: {self.edad}
            pais: {self.pais}
        """)

    # list subclass use.
    _subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # contiene los nombres de las que heredan
        myUsuario._subclasses.append(cls)

    # code to print--> print(myPersona._subclasses)

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#


class myEmpleado(myUsuario):
    def __init__(self, nombre, apellido, edad, pais, cargo, salario):
        super().__init__(nombre, apellido, edad, pais)
        self.cargo = cargo
        self.salario = salario

    def printSoloEmpleado(self):
        print(f"""
            Datos Solo Empleado  -->
                Cargo: {self.cargo}
                Salario: {self.salario}
        """)

    def printEmpleadoCompleto(self):
        print(f"""
            Datos Del Empleado Completos -->
                nombre: {self.nombre}
                apellido: {self.apellido}
                edad: {self.edad}
                pais: {self.pais}
                Cargo: {self.cargo}
                Salario: {self.salario}
        """)

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#


class mySeguro(myEmpleado):
    def __init__(self, nombre, apellido, edad, pais, cargo, salario, aseguradora, estado):
        super().__init__(nombre, apellido, edad, pais, cargo, salario,)
        self.aseguradora = aseguradora
        self.estado = estado

    def printSoloSeguro(self):
        print(f"""
            Datos Solo Seguro  -->
                Cargo: {self.cargo}
                Salario: {self.salario}
        """)

    def printSeguroCompleto(self):
        print(f"""
            Datos Del Empleado Completos -->
                nombre: {self.nombre}
                apellido: {self.apellido}
                edad: {self.edad}
                pais: {self.pais}
                Cargo: {self.cargo}
                Salario: {self.salario}
                Seguro: {self.aseguradora}
                Estado: {self.estado}
        """)


# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# --> Data

objeto1 = myUsuario("Rick", "Sanchez", "40", "USA")
objeto2 = myEmpleado("Rick", "Sanchez", "40", "USA", "lider", "1")
objeto3 = mySeguro("Rick", "Sanchez", "40", "USA",
                   "lider", "1", "Dingerbol", "privado")

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# --> Testing

objeto1.printSoloEmpleado()
# objeto1.printSoloUsuario()
# objeto1.printSoloEmpleado()

# -----#-----#-----#-----#-EXTRA-#-----#-----#-----#-----#-----#

# tengo una super clase
# que tiene la funcion "__init_subclass__"
# y cambia el atributo "default_name" mediante la funcion "__init_subclass__"
# cls se ref a las subclass que heredan de la superclass

# cls se refiere a las subclases que se heredan.
# Los argumentos (**kwargs) que se dan a una nueva clase.
# se pasan a la clase principal hacia el metodo "__init_subclass__"
# Para compatibilidad con otras subclases que usan __init_subclass__, se deben eliminar los argumentos de palabras clave necesarios y pasar los demás a la clase base (Superclase).


class SuperClass:
    def __init_subclass__(cls, **kwargs):
        cls.default_name = "Inherited Class"


class SubClass(SuperClass):
    default_name = "SubClass"  # an attribute of SubClass
    print(default_name)


subclass = SubClass()

print(subclass.default_name)
