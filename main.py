#Exercice 2 de la section 1.1 Mathématiques discretes

#Question a: fonction qui calcul la somme de 2i + 1 allant de i=1 a n
def calcul_a(n: int) -> int:
    somme = 0
    for i in range (1, n+1, 1): 
        somme += 2*i + 1
    return somme 

#Question b: fonction qui calcul la somme de 2i + 1 allant de i=1 a n ecrite avec une boucle while
def calcul_b(n: int) -> int:
    compte, somme = 1, 0
    while compte <= n:
        somme += 2*compte + 1
        compte += 1
    return somme


#Question c: fonction qui permet de calculer la somme de 2i + 1 allant de i = 1 a n recursivement. 
def calcul_c(n: int) -> int :
    return 0 if n==0 else 2*n+1 + calcul_c(n-1)


#Question d: fonction qui calcule la somme de i=1 a n carree de la somme j = 1 a i de 2i + j
def calcul_d(n: int) -> int:
    somme = 0
    for i in range(1,(n*n)+1):
        for j in range(1, i+1):
            somme += 2*i + j
    return somme


#Question e: fonction qui retourne le produit de i = 1 a n de i carre + 1
def calcul_e(n: int) -> int:
    p = 1
    for i in range(1, n+1):
        p *= i**2 + 1
    return p

print(calcul_e(5))