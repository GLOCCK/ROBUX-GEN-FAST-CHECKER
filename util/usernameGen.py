from faker import Faker
import random
import string


def nameGen():
    chars = string.ascii_letters
    nums = string.digits
    fake = Faker()

    name = fake.name()
    name = str(name).split()
    name = name[0]

    username = \
        "".join(random.choice(chars) for i in range(2)) + name.lower() + \
        "".join(random.choice(chars) for i in range(3)) + \
        "".join(random.choice(nums) for i in range(3))

    if username.__contains__("."):
        username.replace(".", "")

    return username

# names = open("./names.txt")
# names = names.read()
# name = random.choice(names)
