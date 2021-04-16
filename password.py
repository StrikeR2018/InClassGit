import random
import string


def passwordGenerate(num) :
    alph = string.ascii_letters+string.digits
    str_password = str().join((random.SystemRandom()).choice(alph) for _ in range(num))
    print("The generated password: " + str_password)

num = int(input("Enter a number for the length of the password："))
passwordGenerate(num)