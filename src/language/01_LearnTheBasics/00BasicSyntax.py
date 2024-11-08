#//-----//-----//-----//-----//-----//-----//-----//-----//-----//
# 00BasicSyntax
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
