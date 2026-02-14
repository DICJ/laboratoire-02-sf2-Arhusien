import random
from fonctions import utils
from classes.Guerrier import Guerrier

class Berserker(Guerrier):
    """
    Représente un berserker et permet sa gestion.
    """

    def __init__(self, nom: str, vie: int, attaque: int, force: int):
        super().__init__(nom, vie, attaque, force)

    def attaquer(self) -> int:
        """
        Détermine la puissance d'une attaque du berserker.

        Returns:
            (int): Le nombre de dégâts de l'attaque.
        """

        # Calculer le nombre de dégâts de l'attaque (et convertir en integer)
        nb_degats_attaque = int(self.attaque + (self.force / 2) + random.randint(-2, 2))
        # Ajouter 5 dégâts par tranche de 10 points de vie perdus
        nb_degats_attaque += ((self._vie_max - self.vie) // 10) * 5

        return nb_degats_attaque
    
    def subir_degats(self, nb_degats: int) -> int:
        """
        Fait subir un certain nombre de dégâts au berserker.

        Parameters:
            nb_degats (int): Le nombre de dégâts à faire subir.

        Returns:
            (int): Le nouveau nombre de points de vie du berserker.
        """

        # Calculer le pourcentage inital des points de vie du personnage
        pourcentage_inital = self._vie / self._vie_max

        # Récupérer le nombre de dégâts encaissés par l'armure
        durete_armure = self.armure.durete

        # Calculer le nombre de dégâts
        nb_degats -= durete_armure
        # Si le nombre de dégâts est négatif
        if nb_degats < 0:
            nb_degats = 0

        # Retirer le nombre de dégâts à la vie du personnage
        self._vie -= nb_degats

        # Calculer le pourcentage final des points de vie du personnage
        pourcentage_final = self._vie / self._vie_max

        # Si le pourcentage inital est supérieur ou égal à 50% et que le pourcentage final est inférieur à 50%
        if pourcentage_inital >= 0.5 and pourcentage_final < 0.5:
            print(f"Le berserker {self.nom} est en FUREUR !")

        return self._vie