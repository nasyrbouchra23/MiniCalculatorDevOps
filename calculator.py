def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("Addition :", add(10,5))
print("Soustraction :", sub(10,5))



















def mult(a, b):
    return a * b
print("Multiplication :", mult(10,5))

def div(a, b):
    return a / b
print("Division :", div(10,5))

def mod(a, b):
    return a % b

print("mod :",mod(10, 3))

def carre(x):
    return x * x

print("carre :",carre(5))


def factorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat = resultat * i
    return resultat

print("factorielle :",factorielle(5))