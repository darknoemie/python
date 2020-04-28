import sys
import Figure


class Cercle(Figure.Figure):
    def __init__(self, nom):
        # Appel du constructeur de la classe de base
        # super(Figure).__init__(nom)
        # Figure.__init__(nom)
        self.nom = nom
        self.rayon = 10
        self.x = 150
        self.y = 150

    def affiche(self):
        sys.stdout.write(
            "{2},rayon={3},x={0},y={1}".format(self.x, self.y, self.nom, self.rayon)
        )
