#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# 01 Learning Variables & DataTypes
#//-----//-----//-----//-----//-----//-----//-----//-----//-----//

"""
- Conceptos Base:

    - que es una variable:
        es el valor que guarda o contiene, una variable.

    - que es un tipo de dato:
        es el tipo de valor, que contiene una variable.

    - para que sirven:
        para almacenar un valor.

"""

# ejemplo: la variable se llama "var1" y es de tipo "entero" y su valor es de "5"
var1 = 5

#//-----//-----//-----//
#   DataTypes
#//-----//-----//-----//

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType

#//-----//-----//-----//
#   Example - DataTypes
#//-----//-----//-----//

var_str         = "Junior your father"
var_int         = 25
var_float       = 25.2
var_complex     = 1j
var_list        = ["butifarra", "morcilla", "chontaduro"]
var_tuple       = ("butifarra", "morcilla", "chontaduro")
var_range       = range(6)
var_dict        = {"name" : "Carlitos", "age" : 27}
var_set         = {"butifarra", "morcilla", "chontaduro"}
var_frozenset   = frozenset({"butifarra", "morcilla", "chontaduro"})
var_bool        = True
var_bytes       = b"YourMother"
var_bytearray   = bytearray(5)
var_memoryview  = memoryview(bytes(5))
var_NoneType    = None

#//-----//-----//-----//
#   Check - DataTypes
#//-----//-----//-----//

print(type(var_str))
print(type(var_int))
print(type(var_float))
print(type(var_complex))
print(type(var_list))
print(type(var_tuple))
print(type(var_range))
print(type(var_dict))
print(type(var_set))
print(type(var_frozenset))
print(type(var_bool))
print(type(var_bytes))
print(type(var_bytearray))
print(type(var_memoryview))
print(type(var_NoneType))

#//-----//-----//-----//
#   Example - Variables
#//-----//-----//-----//

VarString1 = 'usando comillas simples' # Use single quotes
VarString2 = "usando comillas dobles" # Use double quotes
VarString3 = '''simples triples''', """triples dobles""" # Use triple quotes

VarBool1 = True
VarBool2 = False

"""

- Conclusiones:

- existen dos formas de interpretar los tipos de datos
    de forma conceptual y de forma estricta (Programación).

- al inicio de esta guia, yo los presento de forma estricta
    y al final de esta guia de forma conceptual.
    te recomiendo aprenderte la forma conceptual.

- Tipos de datos (Conceptual):

    - Texto
        str
    - Numericos
        int
        float
        complex
    - Collección
        list
        tuple
        sets
        dic
    - Bynarios
        bytes
        bytearray
        memoryview
    - Boolean
        and
        or
        not
    - None

- Colleccion Types

                    List    Tuples      Set     Dict

    Duplicates      Yes     Yes         No      No
    Indexed         Yes     Yes         No      No
    Ordered         Yes     Yes         No      Yes
    Changeable      Yes     No          No      Yes

"""

