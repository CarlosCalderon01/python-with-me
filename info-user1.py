import random, string
# ----- # ----- # ----- # Create string ramdon minus and mayus # ----- # ----- # ----- #
def randomText(size):
    data = string.ascii_lowercase + string.ascii_uppercase
    res = ''.join([random.choice(data) for n in range(size)])
    return res

# ----- # ----- # ----- # Create string ramdon Tag-Email # ----- # ----- # ----- #
def randomTagEmail():
    collect_data = "@hotmail.com", "@live.com", "@outlook.com", "@gmail.com";
    res = ''.join([random.choice(collect_data)])
    return res
# ----- # ----- # ----- # Create Email # ----- # ----- # ----- #



# ----- # ----- # ----- # Create string testing # ----- # ----- # ----- #

# peticion1 = randomText(15);
peticion2 = randomTagEmail();
print(peticion2)

# Objetivo --> # id, name, alfa2 , alfa3 , phone, num
