class myUsuario():
    def __init__(self, nombre, apellido, edad, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pais = pais

    def printSoloUsuario(self):
        print(f"""
            Datos Solo Usuario-->
            nombre: {self.nombre}
            apellido: {self.apellido}
            edad: {self.edad}
            pais: {self.pais}
        """)


class myTrabajo():
    def __init__(self, cargo, salario):
        self.cargo = cargo
        self.salario = salario

    def printSoloTrabajo(self):
        print(f"""
            Datos Solo Trabajo  -->
                Cargo: {self.cargo}
                Salario: {self.salario}
        """)


class mySeguro():
    def __init__(self, aseguradora, estado):
        self.aseguradora = aseguradora
        self.estado = estado

    def printSoloSeguro(self):
        print(f"""
            Datos Solo Seguro  -->
                Cargo: {self.cargo}
                Salario: {self.salario}
        """)

# //-----//-----//-----//-----//-----//-----//-----//-----//-----//


class myEmpleadov1(myUsuario, myTrabajo):
    def __init__(self, nombre, apellido, edad, pais, cargo, salario, num_empleado, horas_max):
        myUsuario.__init__(self, nombre, apellido, edad, pais)
        myTrabajo.__init__(self, cargo, salario)
        self.num_empleado = num_empleado
        self.horas_max = horas_max

    def printSoloMyEmpleado(self):
        print(f"""
            Datos Solo Seguro  -->
                nombre: {self.nombre}
                apellido: {self.apellido}
                edad: {self.edad}
                pais: {self.pais}
                Cargo: {self.cargo}
                Salario: {self.salario}
                Salario: {self.num_empleado}
                Cargo: {self.horas_max}
        """)


class myEmpleadov2(myUsuario, myTrabajo, mySeguro):
    def __init__(self, nombre, apellido, edad, pais, cargo, salario, aseguradora, estado, num_empleado, horas_max):
        myUsuario.__init__(self, nombre, apellido, edad, pais)
        myTrabajo.__init__(self, cargo, salario)
        mySeguro.__init__(self, aseguradora, estado)
        self.num_empleado = num_empleado
        self.horas_max = horas_max

    def printSoloMyEmpleado(self):
        print(f"""
            Datos Solo Seguro  -->
                nombre: {self.nombre}
                apellido: {self.apellido}
                edad: {self.edad}
                pais: {self.pais}
                cargo: {self.cargo}
                salario: {self.salario}
                aseguradora: {self.aseguradora}
                estado: {self.estado}
                num_empleado: {self.num_empleado}
                horas_max: {self.horas_max}
        """)

    def printSoloUsuario():
        print ("Hola, soy la func de la instancia")
    
    def callfunctionsuperclass1(self):
        # super --> sirve para indicar que quiero invocar las funciones de la superclase o clase base.
         return f'{super().printSoloUsuario()}'
    
    def callfunctionsuperclass2(self):
        # super --> sirve para indicar que quiero invocar las funciones de la misma clase de la instancia .
         return f'{self.printSoloUsuario()}'

# //-----//-----//-----//-----//-----//-----//-----//-----//-----//

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# --> Data


objeto4 = myEmpleadov1("Rick", "Sanchez", "40", "USA",
                       "lider", "1", "31231413", "8")
objeto5 = myEmpleadov2("carlos", "calderon", "23", "cali",
                       "trabajador", "11", "adasd", "publico", "31231413", "34")

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# --> Testing

# Use self func of class {myEmpleado} v1-v2
objeto4.printSoloMyEmpleado()
objeto5.printSoloMyEmpleado()

# I can use func superclass
objeto4.printSoloTrabajo()
objeto5.printSoloTrabajo()


objeto5.printSoloSeguro()

# objeto1.printSoloUsuario()
# objeto1.printSoloEmpleado()

# Como saber si e suna subclase

# herencia = issubclass()
herencia = issubclass(myEmpleadov1, myTrabajo)
# instancia = isinstance(instancia, class)
instancia = isinstance(objeto5, myUsuario)

print(herencia)
print(instancia)

class Vehiculo:
    def mover(self):
        print("Moviéndose")

class Auto(Vehiculo):
    def mover(self):
        print("Conduciendo el auto")

test = Auto()

test.mover()

# -----#-----#-----#-----#-----#-----#-----#-----#-----#-----#