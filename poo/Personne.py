class Personne:
    def __init__(self):
        self.nom = "Hendrix"
        self._datenaissance = "1989-05-22"
        self._prenom = "jimi"

    def getNom(self):
        return self.nom

    # Creation d'une propriete
    def _getDatenaissance(self):
        return self._datenaissance

    def _setDatenaissance(self, value):
        self._datenaissance = value

    datenaissance = property(_getDatenaissance, _setDatenaissance)

    # Propriete avec decorateurs
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value
