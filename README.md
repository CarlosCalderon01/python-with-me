# learn-python

# Summary

- This programming project was created with a purpose: to facilitate and aid my understanding of the Python programming language, through teaching and educating new programmers. It emphasizes on creating new content for explaining these concepts.

- As an additional point, it is clarified that the project will utilize freely available community content, specifically the Python Study Guide from the RoadMap platform, as a structured guide for learning the topics covered by the language.

# General objective

- A todo sobre Python recorriendo cada uno de los elementos de RoadMap incluyendo componentes faciles, intermedios y avanzados.

# Specific objectives

- To traverse each of the roadmap elements from start to finish, and from lower to higher difficulty.

- To create examples for each of the elements covered.

- To draft a concluding text summarizing all topics as a review method.

# Bibliography

- Link to view Python in RoadMaps [Link!](https://roadmap.sh/python)

- Link to access my progress in RoadMaps [Link!](https://roadmap.sh/python?s=664e7e5fd6b907c7f7638e17)

- My progress

    - Funciones por defecto de python (acortan codigo)
        Reference: [My progress Link](https://roadmap.sh/python?s=645ab341f3d9ecfa51d91427)

## Abstract 

- This programming project was created with a purpose. Facilitate and help the understanding of the Python programming language through teaching and education. Through the creation of content and the registration of teaching material. That is why I have made the decision to create my own programming book.

## General objective

- Teach Python to learn Python

## Specific objectives

- Learn the use of basic syntax.

- Learn object-oriented programming.

- Build and solve programming problems.

## List of topics spoken

### Learn the use of basic syntax.

### Learn object-oriented programming.

### Build and solve programming problems.

### List Data Types

| Name  | Type  |
| :------------: | :---------------: |
| Text Type | str |
| Numeric Types | int , float , complex |
| Sequence Types | list , tuple , range |
| Mapping Type | dict |
| Set Types | set , frozenset |
| Boolean Type | bool |
| Binary Types | bytes , bytearray , memoryview |
| None Type | NoneType |

### Colleccion Types

| Name  | List  | Tuples  | Set  | Dict  |
| :------------: | :---------------: | :---------------: | :---------------: | :---------------: |
| Duplicates | Yes | Yes | No | No
| Indexed | Yes | Yes | No | No
| Ordered | Yes | Yes | No | Yes
| Changeable | Yes | No | No | Yes

- How to detect data types:

````
print(type(variable))
````
- How to declarate example data types:

````
var_str = "Junior your father"
var_int = 25
var_float = 25.2
var_complex = 1j
var_list = ["butifarra", "morcilla", "chontaduro"]
var_tuple = ("butifarra", "morcilla", "chontaduro")
var_range = range(6)
var_dict = {"name" : "Carlitos", "age" : 27}
var_set = {"butifarra", "morcilla", "chontaduro"}
var_frozenset = frozenset({"butifarra", "morcilla", "chontaduro"})
var_bool = True
var_bytes = b"YourMother"
var_bytearray = bytearray(5)
var_memoryview = memoryview(bytes(5))
var_NoneType = None
````

## Condicionales

- Estructuras de Control Secuenciales
- Estructuras de Control de Selección (Decisiones)
- Estructuras de Control de Repetición (Bucles)
- Estructuras de control de transferencia
- Estructuras de Control de Excepciones

## Topic_01 - 02Conditionals:

- tipos de estructura de control:
    - Estructuras de Control de Selección (Decisiones)
        { if , else , elif }
    - Estructuras de Control de Repetición (Bucles)
        { for , while }
    - Estructuras de control de transferencia
        { pass , break , continue , return }

        
## Topic_01 - 03TypeCastingExceptions:

- Estructuras de Control de Excepciones
    - { try , catch , finally }


## Topic_01 - 04FunctionsBuiltinFunctions:

- Funciones ( def )
- Anonymous functions
    - def namefunc( parameters )
    - *args ( Argumento )
    - **kwargs ( Argumento Clave )

- Built-in Functions

    - Funciones por defecto de python (acortan codigo)
        - Reference: [Built-in Functions](https://docs.python.org/3/library/functions.html)

### Commands List Conditionals

| Name  | Command |
| :------------: | :---------------: |
| Secuenciales | up to down |
| Selección (Decisiones) | { if , else , elif } |
| Repetición (Bucles) | { for , while } |
| transferencia | { break , continue , return } |
| transferencia | { try , catch , finally } |

### Author:

- Carlos Alberto Calderón Barrios ( LearnWithCarlitos@gmail.com )

## Bibliografia

- [Original RoadMap](https://roadmap.sh/python)

- [My Progress RoadMap](https://roadmap.sh/python?s=645ab341f3d9ecfa51d91427)




# Topic_01 - Learn the Basics

## Topic_01 - 00BasicSyntax:

Identificadores en python - Python Identifier -->
    names used to identify {variables, funciones, clases, mmodulos u otros}

- My Naming Conventions:
    - Class --> UpperCamelCase
    - funct --> LowerCamelCase
    - Const --> UPPER_CASE
    - Var --> Snake_case

## Topic_01 - 01VariablesDataTypes:

- Text Type: str
- Numeric Types: int, float, complex
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Boolean Type: bool
- Binary Types: bytes, bytearray, memoryview
- None Type: NoneType

```python
var_String = "Hello World"
var_int = 20
var_float = 20.5
var_complex = 1j
var_list = ["apple", "banana", "cherry"]
var_tuple = ("apple", "banana", "cherry")
var_range = range(6)
var_dict = {"name" : "John", "age" : 36}
var_set = {"apple", "banana", "cherry"}
var_frozenset = frozenset({"apple", "banana", "cherry"})
var_bool = True
var_bytes = b"Hello"
var_bytearray = bytearray(5)
var_memoryview = memoryview(bytes(5))
var_NoneType = None
```






## Topic_01 - 05ListsTuplesSetsDictionaries:

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

## Enviroment

- pip install virtuaenv
- python -m venv myenv (Version mayor a 3.3)
- virtualenv myenv (Version menor a 3.3)
    - .\myenv\Scripts\activate
    - deactivate

## Requirements:
- How to save
    - pip freeze > requirements.txt (lista y guarda producciòn)
    - pip install -r requirements.txt (lee e instala lista)



# End
