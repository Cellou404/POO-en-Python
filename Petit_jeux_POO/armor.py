from joueur import Player

class Armor:
    def __init__(self, nom, puissance):
        self.nom = nom
        self.puissance = puissance
        
    def get_nom_d_armure(self):
        return self.nom
    
    def get_puissance_armure(self):
        return self.puissance
    