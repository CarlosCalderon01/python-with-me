#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# 03 Type Casting Exceptions
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

#   The TypeCasting

"""
    # Python Implicit Type Conversion -->

        Convierte datos de forma automatica y segura.
            El propio lenguaje de python decipna el "tipo de variable"

    # Python Explicit Type Conversion

        Convierte datos de forma manual y forzada.
            ejemplo: { int() ,  float (), etc...}
"""
# Ejemplos -->

numero = int("42")  # Convierte la cadena "42" en el entero 42
numero = float("3.14")  # Convierte la cadena "3.14" en el flotante 3.14
cadena = str(42)  # Convierte el entero 42 en la cadena "42"
booleano = bool(42)  # Convierte el entero 42 en True

tupla = (1, 2, 3)
lista = list(tupla)  # Convierte la tupla en una lista

lista = [1, 2, 3]
tupla = tuple(lista)  # Convierte la lista en una tupla

caracter = chr(65)  # Convierte el número 65 en el carácter 'A'
numero = ord('A')  # Convierte el carácter 'A' en el número 65
numero_complejo = complex(3, 4)  # Crea el número complejo 3 + 4i

lista = [1, 2, 2, 3, 4]
conjunto = set(lista)  # Convierte la lista en un conjunto sin duplicados

# Exceptions

"""

try --> le permite probar un bloque de código en busca de errores.
except - El except bloque le permite manejar el error.
else - El else bloque te permite ejecutar código cuando no hay ningún error.
finally - El finally bloque le permite ejecutar código, independientemente del resultado de los bloques try y except.

{ assert ,  raise } { try , except , else , finally }

Dos tipos de errores. errores de sintaxis, errores de excepción



"""

# Ejemplo 1
"""
try:
    # code that may cause exception
except:
    # code to run when exception occurs
"""

# Ejemplo 2
"""
    try:
        
        even_numbers = [2,4,6,8]
        print(even_numbers[5])

    except ZeroDivisionError:
        print("Denominator cannot be 0.")
        
    except IndexError:
        print("Index Out of Bound.")

    # Output: Index Out of Bound
"""

# Ejemplo 2
"""
    # program to print the reciprocal of even numbers

    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0
    except:
        print("Not an even number!")
    else:
        reciprocal = 1/num
        print(reciprocal)
"""

# Ejemplo 2
"""
    try:
        numerator = 10
        denominator = 0

        result = numerator/denominator

        print(result)
    except:
        print("Error: Denominator cannot be 0.")
        
    finally:
        print("This is finally block.")
"""

# Ejemplo 2
"""

"""