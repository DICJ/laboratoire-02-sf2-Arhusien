import random
from fonctions import utils
from classes.Personnage import Personnage

class Mage(Personnage):
    """
    Représente un mage et permet sa gestion.
    
    Attributes:
        mana (int): Le niveau de mana du mage.
    """

    def __init__(self, nom: str, vie: int, attaque: int, mana: int):
        super().__init__(nom, vie, attaque)

        self._mana = 0
        self.mana = mana

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, valeur_mana):
        # Si la nouvelle valeur mana n'est pas de type int ou de type float
        if not isinstance(valeur_mana, (int, float)):
            raise TypeError("« Mana » doit être de type « int ».")
        
        # Si la nouvelle valeur mana n'est pas comprise entre 0 et 100
        if not utils.est_dans_intervalle(valeur_mana, 0, 100):
            raise ValueError("« Mana » doit être compris entre 0 et 100.")

        # Définir la nouvelle valeur mana (et convertir en integer)
        self._mana = int(valeur_mana)
        
    def attaquer(self) -> int:
        """
        Détermine la puissance d'une attaque du mage.

        Returns:
            (int): Le nombre de dégâts de l'attaque.
        """

        nb_degats_attaque = self.attaque
        # S'il reste du mana
        if self.mana > 0:
            # Ajouter 60 au nombre de dégâts de l'attaque
            nb_degats_attaque += 60

        # Diminuer le niveau de mana du mage
        self._diminuer_mana()
        
        # Retourner le nombre de dégâts de l'attaque (et convertir en integer)
        return int(nb_degats_attaque)

    def _diminuer_mana(self):
        """
        Diminue les réserves de mana du mage.

        Returns:
            (int): Le nouveau niveau de mana du mage.
        """

        # Retirer entre 15 et 25 de mana
        self._mana -= random.randint(15, 25)

        return self._mana
