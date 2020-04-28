import sys
import Personne

personne = Personne.Personne()

sys.stdout.write("nom=" + personne.nom + "\n")
sys.stdout.write("nom=" + personne.getNom() + "\n")

personne.datenaissance = "1990-10-04"
sys.stdout.write("date naissance=" + personne.datenaissance + "\n")

personne.prenom = "Jimi"
sys.stdout.write("prenom=" + personne.prenom + "\n")

# Afficher les attributs et les methodes d'un objet
print("\n--- Afficher les attributs et les methodes d'un objet ---")
for str in dir(personne):
    sys.stdout.write(str + ",")

# Afficher les attributs d'un objet
print("\n--- Afficher les attributs d'un objet ---")
for key, value in personne.__dict__.items():
    sys.stdout.write(key + "=" + value + ",\n")
print("")
