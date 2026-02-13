import random
from fonctions import utils
from classes.Personnage import Personnage
from classes.Armure import Armure

class Guerrier(Personnage):
    """
    Représente un guerrier et permet sa gestion.
    
    Attributes:
        force (int): La force du guerrier.
    """

    def __init__(self, nom: str, vie: int, attaque: int, force: int):
        armure = Armure(
            nom="Armure de plaques",
            durete=12
        )

        super().__init__(nom, vie, attaque, armure)

        self._force = 1
        self.force = force
    
    @property
    def force(self):
        return self._force
    
    @force.setter
    def force(self, valeur_force):
        # Si la nouvelle valeur force n'est pas de type int ou de type float
        if not isinstance(valeur_force, (int, float)):
            raise TypeError("« Force » doit être de type « int ».")
        
        # Si la nouvelle valeur force n'est pas comprise entre 1 et 50
        if not utils.est_dans_intervalle(valeur_force, 1, 50):
            raise ValueError("« Force » doit être compris entre 1 et 50.")

        # Définir la nouvelle valeur force (et convertir en integer)
        self._force = int(valeur_force)
    
    def attaquer(self) -> int:
        """
        Détermine la puissance d'une attaque du guerrier.

        Returns:
            (int): Le nombre de dégâts de l'attaque.
        """

        # Calculer le nombre de dégâts de l'attaque (et convertir en integer)
        nb_degats_attaque = int(self.attaque + (self.force / 2) + random.randint(-2, 2))

        return nb_degats_attaque
