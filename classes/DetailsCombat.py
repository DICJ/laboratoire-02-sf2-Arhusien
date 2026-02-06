from classes.Personnage import Personnage

class DetailsCombat:
    """
    Représente un combat, permet d'afficher les détails de celui-ci et de les mettre à jour.
    
    Attributes:
        lst_combattants (list[Personnage, Personnage]): Une liste contenant l'attaquant et le défenseur (dans cet ordre).
    """

    def __init__(self, lst_combattants: list[Personnage, Personnage]):
        self._lst_combattants = lst_combattants
        self._vainqueur = None
        self._nb_tours = 0

    @property
    def nb_tours(self):
        return self._nb_tours
    
    @property
    def vainqueur(self):
        return self._vainqueur
    
    @vainqueur.setter
    def vainqueur(self, valeur_vainqueur: Personnage):
        # Si la nouvelle valeur vainqueur n'est pas une instance de la classe Personnage ou une instance d'une classe enfant
        if not isinstance(valeur_vainqueur, Personnage):
            raise TypeError("« Vainqueur » doit être de type « Personnage » ou d'une instance de classe enfant à « Personnage ».")
        
        # Définir la nouvelle valeur vainqueur
        self._vainqueur = valeur_vainqueur

    def incrementer_nb_tours(self) -> int:
        """
        Icrémente de un le nombre de tours du combat.

        Returns:
            (int): Le nouveau nombre de tours du combat.
        """

        # Incrémenter de un le nombre de tours
        self._nb_tours += 1

        return self._nb_tours

    def __str__(self):
        return f"🜲 {self._vainqueur.nom} / ↻ {self._nb_tours}"
