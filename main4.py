import random
import string

class MyGenerateCountrys():
    def __init__(self, name, alfa2, alfa3, phone, num):
        self.name = name
        self.alfa2 = alfa2
        self.alfa3 = alfa3
        self.phone = phone
        self.num = num

    @classmethod
    def generate_random_country(cls):
        # Genera valores aleatorios para los atributos de la clase
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        alfa2 = ''.join(random.choices(string.ascii_uppercase, k=2))
        alfa3 = ''.join(random.choices(string.ascii_uppercase, k=3))
        phone = ''.join(random.choices(string.digits, k=4))
        num = random.randint(1, 999)

        # Crea y devuelve una instancia de la clase con los valores aleatorios
        return cls(name, alfa2, alfa3, phone, num)

# Ejemplo de uso
random_country = MyGenerateCountrys.generate_random_country()
print("Nombre:", random_country.name)
print("Alfa2:", random_country.alfa2)
print("Alfa3:", random_country.alfa3)
print("Teléfono:", random_country.phone)
print("Número:", random_country.num)
