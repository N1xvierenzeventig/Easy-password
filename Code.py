from random import *
def password_giver():
    a = ("abcdefghijklmnopqrstuvwxyz")
    b = a.upper()
    c = ("1234567890;'./<>,")
    d = a + b + c
    e = list(d)
    shuffle(e)
    f = "".join(choice(e) for i in range (int(input("How many symbols in your password do you want?: "))))
    return f
print(password_giver())