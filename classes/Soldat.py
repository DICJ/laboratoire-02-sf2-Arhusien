from fonctions import utils
from classes.Personnage import Personnage
from classes.Armure import Armure

class Soldat(Personnage):
    """
    Représente un soldat et permet sa gestion.
    """

    def __init__(self, nom: str, vie: int, attaque: int):
        armure = Armure(
            nom="Cotte de mailles",
            durete=15
        )
        
        super().__init__(nom, vie, attaque, armure)
    
    def subir_degats(self, nb_degats: int) -> int:
        """
        Fait subir un certain nombre de dégâts au soldat.

        Parameters:
            nb_degats (int): Le nombre de dégâts à faire subir.

        Returns:
            (int): Le nouveau nombre de points de vie du soldat.
        """

        # Récupérer le nombre de dégâts encaissés par l'armure
        durete_armure = self.armure.durete

        # Calculer le nombre de dégâts
        nb_degats = (nb_degats - durete_armure) * 0.9
        # Si le nombre de dégâts est négatif
        if nb_degats < 0:
            nb_degats = 0

        # Retirer le nombre de dégâts (converti en integer) à la vie du personnage
        self._vie -= int(nb_degats)

        return self._vie
