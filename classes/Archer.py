import random
from fonctions import utils
from classes.Personnage import Personnage

class Archer(Personnage):
    """
    Représente un archer et permet sa gestion.
    
    Attributes:
        dexterite (int): La dextérité de l'archer.
    """

    def __init__(self, nom: str, vie: int, attaque: int, dexterite: int):
        super().__init__(nom, vie, attaque)

        self._dexterite = 50
        self.dexterite = dexterite
    
    @property
    def dexterite(self):
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self, valeur_dexterite):
        # Si la nouvelle valeur dextérité n'est pas de type int ou de type float
        if not isinstance(valeur_dexterite, (int, float)):
            raise TypeError("« Dexterite » doit être de type « int ».")
        
        # Si la nouvelle valeur dextérité n'est pas comprise entre 50 et 100
        if not utils.est_dans_intervalle(valeur_dexterite, 50, 100):
            raise ValueError("« Dexterite » doit être compris entre 50 et 100.")

        # Définir la nouvelle valeur dextérité (et convertir en integer)
        self._dexterite = int(valeur_dexterite)
    
    def attaquer(self) -> int:
        """
        Détermine la puissance d'une attaque de l'archer.

        Returns:
            (int): Le nombre de dégâts de l'attaque.
        """

        # Générer un nombre entre 0 et 100 et regarder s'il est inférieur à la dextérité
        est_doublee = random.randint(0, 100) < self.dexterite

        # Calculer le nombre de dégâts de l'attaque
        nb_degats_attaque = self.attaque + 15
        # Si l'attaque est doublée
        if est_doublee:
            nb_degats_attaque *= 2

        # Retourner le nombre de dégâts de l'attaque (et convertir en integer)
        return int(nb_degats_attaque)

