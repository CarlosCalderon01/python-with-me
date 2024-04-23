class Motor:
    def arrancar(self):
        print("Motor arrancado")

class Vehiculo:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        print("Vehículo arrancado")
        self.motor.arrancar()

# objeto clase 1
motor_de_auto = Motor()
# objeto clase 2 / le paso objeto clase 1
auto = Vehiculo(motor_de_auto)
# invoco arrancar clase 2 / y luego arrancar sub clase 1
auto.arrancar()

# creo objeto motor de la class Motor
# creo objeto auto de la calse vehiculo y le paso el objeto motor
# ejecutor arrancar del metodo vehiculo y su sub clases

#creo objetos y paso los objetos dentro de otros objetos