#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# 02 Conditionals
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""
    tipos de estructura de control
        1- Estructuras de Control Secuenciales
        2- Estructuras de Control de Selección (Decisiones)
        3- Estructuras de Control de Repetición (Bucles)
        4- Estructuras de control de transferencia
        5- Estructuras de Control de Excepciones

    1- Estructuras de Control Secuenciales
        Estas estructuras funcionan una después de la otra
        siguen sin ningún problema de arriba a abajo,
        no cambian mucho el orden de ejecución del código.

    2- Estructuras de Control de Selección (Decisiones)
        Estas sirven para que podamos tomar decisiones,
        además de poder ejecutar diferentes bloques de nuestro código
        según la condición.
        { if , else , elif }

    3- Estructuras de Control de Repetición (Bucles)
        Estas sirven para repetir secciones de código
        un número determinado o indeterminado de veces.
        { for , while }

    4- Estructuras de control de transferencia
        Estas sirven para transferirnos a otros bloques de código más específicos.
        { break , continue , return }

    5- Estructuras de Control de Excepciones
        Estas sirven para el manejo de los errores y las excepciones de una manera más controlada.
        { try , catch , finally }

"""

"""
    tipos de estructura de control
        1- Estructuras de Control Secuenciales
            arriba a abajo (puedes ignorar)
        2- Estructuras de Control de Selección (Decisiones)
            { if , else , elif }
        3- Estructuras de Control de Repetición (Bucles)
            { for , while }
        4- Estructuras de control de transferencia
            { break , continue , return }
        5- Estructuras de Control de Excepciones
            { try , catch , finally }
"""

# EXAMPLE --> 

#//-----//-----//-----//
#   Example - Selección { if , else , elif }
#//-----//-----//-----//

edad = 20

if edad > 18:
    print("eres mayor de edad")
elif edad < 18:
    print("eres menor de edad")
elif edad == 18:
    print("Felicidades ya eres adulto")
else:
    print("error al ingresar el numero")

#//-----//-----//-----//
#   Example - Repetición { for , while }
#//-----//-----//-----//

N_Contador = 0

while N_Contador < 10: # Ejecutar mientras
    print("Valor Actual Es: ", N_Contador) # Resultado
    N_Contador += 1 # hacer incremento

# Arreglo de numeros
NumberList = [1, 2, 3, 4, 5]

for num in NumberList: # Ciclo for
    print(num) # Imprimir cada numero

# Iterar para cada ca
# racter del string "Carlitos"
for char in "Carlitos":
    print(char)

#//-----//-----//-----//
#   Example - transferencia { break , continue , return }
#//-----//-----//-----//

for numero in range(10): 
    if numero == 5: # Cuando numero sea igual a 5
        break   # Sale
    print(numero) # imprimir

for numero in range(10): # numeros del 0 al 10
    if numero % 2 == 0: # Solo si son numeros impares
        continue  # Salta a la siguiente iteración si num es par
    print(numero)

#//-----//-----//-----//
#   Example - Excepciones
#//-----//-----//-----//
