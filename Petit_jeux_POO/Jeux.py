# Programme principal

from joueur import Player
from weapon import Weapon
from armor import Armor

# ici on créer des instances des classes Player, Weapon et Armor
arme = Weapon("un pistolet", 13)
arme2 = Weapon("une fleche", 10)
joueur1 = Player("Cellou", 100, 40)
joueur2 = Player("Karamo", 100, 45)
armure1 = Armor("une armure corporelle", 34)
armure2 = Armor("une ceramique blindée", 50)

print("\n*********************************************************************************")

# Joueur 2 attaque le Joueur 1 avec ses points d'attaque et porte une armure 

joueur1.attack_joueur(joueur2)
print(joueur1.get_pseudo(), "attaque", joueur2.get_pseudo(), "avec ",arme.get_nom(), 
      "et ", armure1.get_nom_d_armure())

print(joueur2.get_pseudo(), "Vous avez subit:", (joueur1.get_pointsAttack() + arme.get_nombreDegat()), 
      "points d'attaque. Votre point de vie est maintenant:", (joueur2.get_vie() + armure1.get_puissance_armure() - arme.get_nombreDegat()))

print("\n*********************************************************************************")

# Joueur 1 attaque le Joueur 2 avec ses point d'attaque et porte une armure 

joueur2.attack_joueur(joueur1)
print(joueur2.get_pseudo(), "attaque", joueur1.get_pseudo(), "avec ", arme2.get_nom(), 
      "et ",armure2.get_nom_d_armure())

print(joueur1.get_pseudo(), "Vous avez subit:", (joueur2.get_pointsAttack() + arme2.get_nombreDegat()), 
      "points d'attaque. Votre point de vie est maintenant:", (joueur1.get_vie() + armure2.get_puissance_armure() - arme2.get_nombreDegat()))
