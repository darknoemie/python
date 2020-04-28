# Retourne une liste des nombres premiers de 2 a x
def cribleEratosthenes(x):
    liste = [2]

    # construire une liste avec des nombres impairs apres 2
    for i in range(3, x, 2):
        liste.append(i)

    # supprimer les nombres non premiers
    for i in liste:
        for n in liste:
            if n % i == 0 and i != n:
                liste.remove(n)

    return liste


# Appel de la fonction
# print(cribleEratosthenes(20))
