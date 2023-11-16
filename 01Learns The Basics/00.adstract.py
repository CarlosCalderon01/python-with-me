#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 0 - Note Me
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""
    i want to help you. beacuse.
    i make this module for adstract all info on python.
    for a  faster read and remember info in the future.
    this content is make from pageweb roadmap.sh in this module python

    by. Carlos Alberto Calderon Barrios
"""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 1 - Basic_Syntax
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""
    Identificadores en python - Python Identifier -->

        names used to identify {variables, funciones, clases, mmodulos u otros}

    My Naming Conventions -->

        Class --> UpperCamelCase
        funct --> LowerCamelCase
        Const --> UPPER_CASE
        Var   --> Snake_case
"""
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 2 - Variables_DataTypes
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""
    Text Sequence Type -->          str
    Numeric Types -->               int, float, complex 
    Sequence Types -->              list, tuple, range
    Boolean Operations -->	        and . or ,  not
    Binary Sequence Types -->       bytes, bytearray, memoryview
    Set Types -->	                set, frozenset
    Mapping Types -->	            dict

    Additional Features -->
    Numeric Types --> fractions.Fraction , decimal.Decimal

"""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 3 - Conditionals or Control_Structures
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""
    tipos de estructura de control
        1- Estructuras de Control Secuenciales
        2- Estructuras de Control de Selección (Decisiones)
        3- Estructuras de Control de Repetición (Bucles)
        4- Estructuras de control de transferencia
        5- Estructuras de Control de Excepciones

    1- Estructuras de Control Secuenciales
        ejecutan instrucciones en secuencia. una después de la otra
            en el orden en que se encuentran en el programa
                No alteran el flujo de ejecución de manera significativa.

    2- Estructuras de Control de Selección (Decisiones)
        Permiten que un programa tome decisiones.
            ejecute diferentes bloques de código según ciertas condiciones
                { if , else , elif }

    3- Estructuras de Control de Repetición (Bucles)
        Permiten que se repita un bloque de código múltiples veces.
            ya sea un número específico de repeticiones
                o hasta que se cumpla una condición.
                    { for , while }

    4- Estructuras de control de transferencia
        altera el flujo de ejecución de un programa de manera más específica
            { break , continue , return }

    5- Estructuras de Control de Excepciones
        Estas permiten manejar errores y excepciones de manera controlada
            { try , catch , finally }

"""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 4 - TypeCasting & Exceptions
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

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 5 - Functions, BuiltinFunctions
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

""""""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART 6 - lists, Tuplas, Sets, Dictionaries
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

""""""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART  - 
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

""""""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART  - 
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

""""""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART  - 
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

""""""

#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# PART  - 
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

""""""

# Boolean Operations — and, or, not

"""
    Operation   Result                                  Notes

    x or y      if x is true, then x, else y            (1)
    x and y     if x is false, then x, else y           (2)
    not x       if x is false, then True, else False    (3)

    - This is a short-circuit operator, so it only evaluates the second argument
        if the first one is false.
    - This is a short-circuit operator, so it only evaluates the second argument
        if the first one is true.
    - not has a lower priority than non-Boolean operators
        so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# Comparisons

"""
    Operation   Meaning
    
        <       strictly less than
        <=      less than or equal
        >       strictly greater than
        >=      greater than or equal
        ==      equal
        !=      not equal
        is      object identity
        is not  negated object identity
    
"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# Numeric Types

"""
    abs(x)              absolute value or magnitude of x            abs()
    int(x)              x converted to integer                      int()
    float(x)            x converted to floating point               float()
    complex(re, im)     a complex number with real part re
                            imaginary part im. im defaults to zero. complex()
    c.conjugate()       conjugate of the complex number c
    divmod(x, y)        the pair (x // y, x % y)                    divmod()
    pow(x, y)           x to the power y                            pow()
    x ** y              x to the power y
"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# Bitwise Operations on Integer Types

"""
    Operation   Result

    x | y       bitwise or of x and y
    x ^ y       bitwise exclusive or of x and y
    x & y       bitwise and of x and y
    x << n      x shifted left by n bits
    x >> n      x shifted right by n bits
    ~x          the bits of x inverted

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# Sequence Types — list, tuple, range

"""
    Common Sequence Operations

    Operation               Result

    x in s                  True if an item of s is equal to x, else False
    x not in s              False if an item of s is equal to x, else True
    s + t                   the concatenation of s and t
    s * n or n * s          equivalent to adding s to itself n times
    s[i]                    ith item of s, origin 0
    s[i:j]                  slice of s from i to j
    s[i:j:k]                slice of s from i to j with step k
    len(s)                  length of s
    min(s)                  smallest item of s
    max(s)                  largest item of s
    s.index(x[, i[, j]])    index of the first occurrence of x in s
                                (at or after index i and before index j)
    s.count(x)              total number of occurrences of x in s

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#   Mutable Sequence Types

"""
    Operation               Result

    s[i] = x                item i of s is replaced by x
    s[i:j] = t              slice of s from i to j is replaced by the contents of the iterable t
    del s[i:j]              same as s[i:j] = []
    s[i:j:k] = t            the elements of s[i:j:k] are replaced by those of t
    del s[i:j:k]            removes the elements of s[i:j:k] from the list
    s.append(x)             appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
    s.clear()               removes all items from s (same as del s[:])
    s.copy()                creates a shallow copy of s (same as s[:])
    s.extend(t) or s += t   extends s with the contents of t
                                (for the most part the same as s[len(s):len(s)] = t)
    s *= n                  updates s with its contents repeated n times
    s.insert(i, x)          inserts x into s at the index given by i (same as s[i:i] = [x])
    s.pop() or s.pop(i)     retrieves the item at i and also removes it from s
    s.remove(x)             remove the first item from s where s[i] is equal to x
    s.reverse()             reverses the items of s in place

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

# Text Sequence Type — str

"""
    Textual data in Python is handled with str objects, or strings.
        Strings are immutable sequences of Unicode code points.
            String literals are written in a variety of ways:

"""

# Single quotes: 'allows embedded "double" quotes'

# Double quotes: "allows embedded 'single' quotes"

# Triple quoted: '''Three single quotes''', """Three double quotes"""

"""
    String Methods

    str.capitalize()
    str.casefold()
        lower()
        casefold()

    str.center(width[, fillchar])
    str.count(sub[, start[, end]])
    str.encode(encoding='utf-8', errors='strict')


"""
#-----#-----#-----#-----#-----#-----#-----#-----#-----#



#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#

"""

"""

#-----#-----#-----#-----#-----#-----#-----#-----#-----#
