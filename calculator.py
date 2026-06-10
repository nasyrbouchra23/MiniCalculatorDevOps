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

def moyenne(a, b):
    return (a + b) / 2

print("moyenne :",moyenne(10, 20))

def valeur_absolue(x):
    if x < 0:
        return -x
    return x

print("la valeur absolue :",valeur_absolue(-7))

def puissance(x, n):
    resultat = 1
    for i in range(n):
        resultat = resultat * x
    return resultat

print("puissance :",puissance(2, 3))

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("pgcd :",pgcd(12, 18))