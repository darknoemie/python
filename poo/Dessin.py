import Figure
import Cercle

# Instanciation d'un objet de type Figure
# La variable figure contient une référence sur un objet Figure
figure = Figure.Figure("figure1")
print(dir(figure))

print("\n")
# Appel de la méthode affiche de la classe Figure
figure.affiche()
print("\n")


cercle = Cercle.Cercle("cercle1")
cercle.affiche()

print("")

# help(figure)

print("Utilisation d'une methode de classe")
x = Figure.Figure.cm_getCompteur()
print(x)
print("Utilisation d'une methode static")
y = Figure.Figure.sm_getCompteur()
print(y)
# print(figure.getCompteur())

# Utiliser la fonction speciale __str__ de figure
print("speciale __str__")
print(figure)

# Illustration du polymorphisme
print("-- Illustration du polymorphisme --")
liste = [figure, cercle]
for f in liste:
    f.affiche()
    print()
