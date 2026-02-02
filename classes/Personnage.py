from fonctions import utils

class Personnage:
    """
    Représente un personnage et permet sa gestion.
    
    Attributes:
        nom (str): Le nom du personnage.
        vie (int): Le nombre de points de vie du personnage.
        attaque (int): La puissance d'attaque du personnage.
    """

    def __init__(self, nom: str, vie: int, attaque: int):
        self.nom = nom

        self._vie = 0
        self.vie = vie

        self._attaque = 0
        self.attaque = attaque

    @property
    def vie(self):
        return self._vie

    @vie.setter
    def vie(self, valeur_vie: int):
        # Si la nouvelle valeur vie n'est pas de type int ou de type float
        if not isinstance(valeur_vie, (int, float)):
            raise TypeError("« Vie » doit être de type « int ».")
        
        # Si la nouvelle valeur vie n'est pas comprise entre 0 et 500
        if not utils.est_dans_intervalle(valeur_vie, 0, 500):
            raise ValueError("« Vie » doit être compris entre 0 et 500.")

        # Définir la nouvelle valeur vie (et convertir en int)
        self._vie = int(valeur_vie)

    @property
    def attaque(self):
        return self._attaque

    @attaque.setter
    def attaque(self, valeur_attaque: int):
        # Si la nouvelle valeur attaque n'est pas de type int ou de type float
        if not isinstance(valeur_attaque, (int, float)):
            raise TypeError("« Attaque » doit être de type « int ».")
        
        # Si la nouvelle valeur attaque n'est pas comprise entre 0 et 50
        if not utils.est_dans_intervalle(valeur_attaque, 0, 50):
            raise ValueError("« Attaque » doit être compris entre 0 et 50.")

        # Définir la nouvelle valeur attaque (et convertir en int)
        self._attaque = int(valeur_attaque)

    def subir_degats(self, nb_degats: int):
        """
        Fait subir un certain nombre de dégâts au personnage.

        Parameters:
            nb_degats (int): Le nombre de dégâts à faire subir.

        Returns:
            (int): Le nouveau nombre de points de vie du personnage.
        """

        # Retirer le nombre de dégâts à la vie du personnage
        self.vie -= nb_degats

        return self.vie
