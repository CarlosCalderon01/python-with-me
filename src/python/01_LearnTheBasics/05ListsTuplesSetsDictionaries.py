#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# 05ListsTuplesSetsDictionaries
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""

- Estrucutras que contienen datos. (Facilitan uso)
    - Reference: [Dictionary vs List vs Set vs Tuple](https://jerrynsh.com/tuples-vs-lists-vs-sets-in-python/)

Diferencias clave entre diccionario, lista, conjunto y tupla

- Sintaxis
    - Dictionary: utiliza llaves { } con pares clave-valor separados por comas.
    - List: Emplea corchetes [ ] con elementos separados por comas.
    - Set: utiliza llaves { } con elementos separados por comas.
    - Tuple: Emplea paréntesis ( ) con elementos separados por comas.

- Orden
    - Dictionary: mantiene el orden en Python 3.7+ pero está desordenado en Python 3.6.
    - List: Mantiene el orden.
    - Set: Desordenado.
    - Tuple: Mantiene el orden.

- Datos duplicados
    - Dictionary: las claves son únicas, los valores se pueden duplicar.
    - List: Permite elementos duplicados.
    - Set: No permite elementos duplicados.
    - Tuple: Permite elementos duplicados.

- Indexación
    - Dictionary: indexación basada en claves.
    - List: indexación basada en números enteros a partir de 0.
    - Set: sin mecanismo basado en índices.
    - Tuple: indexación basada en números enteros a partir de 0.

- Elementos de búsqueda
    - Dictionary: utiliza el método get(key) para recuperar el valor de una clave específica.
    - List: utiliza el método index() para buscar y devolver el índice de la primera aparición.
    - Set: Desordenado, por lo que la búsqueda no es aplicable.
    - Tuple: utiliza el método index() para buscar y devolver el índice de la primera aparición.

"""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# Dictionary
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}

nombre = mi_diccionario['nombre']
edad = mi_diccionario['edad']
ciudad = mi_diccionario['ciudad']

print(nombre, edad, ciudad)

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# list
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

mi_lista = [10, 20, 30, 40, 50]

primer_elemento = mi_lista[0]
segundo_elemento = mi_lista[1]
tercer_elemento = mi_lista[2]

print(primer_elemento, segundo_elemento, tercer_elemento)

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# Set
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

mi_conjunto = {1, 2, 3, 4, 5}

if 3 in mi_conjunto:
    print("El conjunto contiene el número 3")

# No se pueden acceder por índice ya que los conjuntos no tienen índices.
# Los elementos en un conjunto no tienen un orden específico.
# Pero puedes verificar la pertenencia de un elemento

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# tuple
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

mi_tupla = (10, 20, 30, 40, 50)

primer_elemento = mi_tupla[0]
segundo_elemento = mi_tupla[1]
tercer_elemento = mi_tupla[2]

print(primer_elemento, segundo_elemento, tercer_elemento)
