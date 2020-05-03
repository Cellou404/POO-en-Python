
class Weapon:

    def __init__(self, nom, degat):
        self.nom = nom
        self.degat = degat

    def get_nom(self):
        return self.nom

    def get_nombreDegat(self):
        return self.degat
