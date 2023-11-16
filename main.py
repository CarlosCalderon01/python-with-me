"""
    que es ASCII --> El código ASCII (American Standard Code for Information Interchange)
    es un sistema de codificación que asigna un valor numérico único a diferentes caracteres
    utilizados en la comunicación electrónica.
"""

import random
import string

# list data char and numbers
list_ascci_lower = string.ascii_lowercase
list_ascci_upper = string.ascii_uppercase
list_numbers_digits = string.digits
list_punctuation = string.punctuation

# Select a random value
random_minus = random.choice(list_ascci_lower)
random_mayus = random.choice(list_ascci_upper)
random_digit = random.choice(list_numbers_digits)
random_punctuation = random.choice(list_punctuation)

# for x in "ABCDEFGHIJ":
#     for j in "1234567890":
#         print( x+" "+j )
