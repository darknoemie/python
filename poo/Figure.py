import sys


class Figure(object):

    # Variable de classe
    compteur = 0

    # Methode de classe , le premier argument doit etre cls
    @classmethod
    def cm_getCompteur(cls):
        return cls.compteur

    # Deuxieme methode  de classe
    @staticmethod
    def sm_getCompteur():
        return Figure.compteur

    # Constructeur
    def __init__(self, nom):
        """ variable d'instance """
        self.nom = nom
        self.couleur = "rouge"
        Figure.compteur += 1

    def affiche(self):
        sys.stdout.write("figure nom=" + self.nom)

    # getCompteur = classmethod(getCompteur)


#    def __str__(self):
#        return "Figure: nom="+self.nom+",couleur="+self.couleur
