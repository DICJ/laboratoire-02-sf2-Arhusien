import random
from fonctions import utils

class Armure:
    """
    Représente une armure.
    
    Attributes:
        nom (str): Le nom de l'armure.
        durete (int): La dureté de l'armure.
    """

    def __init__(self, nom: str, durete: int):
        self._durete = 0
        self.durete = durete

    @property
    def durete(self):
        return self._durete
    
    @durete.setter
    def durete(self, valeur_durete):
        # Si la nouvelle valeur dureté n'est pas de type int ou de type float
        if not isinstance(valeur_durete, (int, float)):
            raise TypeError("« Durete » doit être de type « int ».")
        
        # Si la nouvelle valeur dureté n'est pas comprise entre 0 et 15
        if not utils.est_dans_intervalle(valeur_durete, 0, 15):
            raise ValueError("« Durete » doit être compris entre 0 et 15.")

        # Définir la nouvelle valeur dureté (et convertir en integer)
        self._durete = int(valeur_durete)
