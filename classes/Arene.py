from classes.Personnage import Personnage

class Arene:
    """
    Représente une arène, permet sa gestion et d'y organiser des combats.

    Attributes:
        lst_persos (list[Personnage]): La liste de personnages initale de l'arène.
    """

    def __init__(self, lst_persos: list[Personnage]):
        self._lst_persos = lst_persos
    
    