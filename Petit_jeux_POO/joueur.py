
class Player:

  def __init__(self, pseudo, vie, attack):
      self.pseudo = pseudo
      self.vie = vie
      self.attack = attack
      print("Bienvenue au joueur:", pseudo, "/Points de vie:", vie, "/Attack: ", attack)

  def get_pseudo(self):
      return self.pseudo

  def get_vie(self):
      return self.vie

  def get_pointsAttack(self):
      return self.attack

  def degat(self, degat):
      self.vie -= degat

  def attack_joueur(self, cible_joueur):
      cible_joueur.degat(self.attack)
