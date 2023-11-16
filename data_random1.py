import random
import string
# ----- # ----- # ----- # Create string ramdon minus and mayus # ----- # ----- # ----- #

def randomMinusAndMayus(size):

    data = string.ascii_lowercase + string.ascii_uppercase
    result = ''.join([random.choice(data) for n in range(size)])
    return result

# ----- # ----- # ----- # Create string ramdon numbers # ----- # ----- # ----- #

def randomDigits(size):

    data = string.digits
    result = ''.join([random.choice(data) for n in range(size)])
    return result


# ----- # ----- # ----- # Create string ramdon punctuation # ----- # ----- # ----- #

def randomPunctuation(size):

    data = string.punctuation
    result = ''.join([random.choice(data) for n in range(size)])
    return result

# ----- # ----- # ----- # Create string ramdon All # ----- # ----- # ----- #

def randomAll(size):

    data = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    result = ''.join([random.choice(data) for n in range(size)])

    return result

# ----- # ----- # ----- # testing # ----- # ----- # ----- #

res1 = randomMinusAndMayus(10)
res2 = randomDigits(10)
res3 = randomPunctuation(10)
res4 = randomAll(10)

print(res1)
