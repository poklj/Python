from math import sqrt
def gcd(x, y):
    """
    find the greatest common denominator between two numbers
    :param x: Int Higher then Y
    :param y: Int Lower then X
    :return: The GCD (Int)
    """
    a = x
    b = y
    while True:
        if a%b != 0:
            c = b
            b = a%b #y
            a = c
        else:
            return b

def My_Sqrt(inp):
    g = 2
    l = 0
    while True:
        if g != l:
            l = g
            y = inp / g
            x = g*y
            g = (g + (x/g))/2
        else:
            return g, sqrt(inp)
# o = ""
# sqrt(o)
print(My_Sqrt(2))
print(gcd(4000375  ,85))