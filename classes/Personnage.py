from fonctions import utils
from classes.Armure import Armure

class Personnage:
    """
    Représente un personnage et permet sa gestion.
    
    Attributes:
        nom (str): Le nom du personnage.
        vie (int): Le nombre de points de vie du personnage.
        attaque (int): La puissance d'attaque du personnage.
        armure (Armure): L'armure du personnage.
    """

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure):
        self.nom = nom

        self._vie = 0
        self.vie = vie

        # Définir la valeur de vie maximale du personnage
        self._vie_max = int(self._vie)

        self._attaque = 0
        self.attaque = attaque

        self._armure = None
        self.armure = armure

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

    @property
    def armure(self):
        return self._armure
    
    @armure.setter
    def armure(self, valeur_armure: Armure):
        # Si la nouvelle valeur armure n'est pas de type Armure
        if not isinstance(valeur_armure, Armure):
            raise TypeError("« Armure » doit être de type « Armure ».")

        # Définir la nouvelle valeur armure
        self._armure = valeur_armure

    def subir_degats(self, nb_degats: int) -> int:
        """
        Fait subir un certain nombre de dégâts au personnage.

        Parameters:
            nb_degats (int): Le nombre de dégâts à faire subir.

        Returns:
            (int): Le nouveau nombre de points de vie du personnage.
        """

        # Récupérer le nombre de dégâts encaissés par l'armure
        durete_armure = self.armure.durete

        # Calculer le nombre de dégâts
        nb_degats -= durete_armure
        # Si le nombre de dégâts est négatif
        if nb_degats < 0:
            nb_degats = 0

        # Retirer le nombre de dégâts à la vie du personnage
        self._vie -= nb_degats

        return self._vie
    
    def reinitialiser_vie(self) -> int:
        """
        Réinitialise la vie du personnage à sa valeur de départ.

        Returns:
            (int): La nouvelle valeur de vie du personnage.
        """

        self._vie = self._vie_max

        return self._vie

    def __str__(self):
        # Récupérer le nom de la classe de l'instance
        type_personnage = type(self).__name__

        return f"{self.nom} ({type_personnage} / {self.vie if self.vie > 0 else 0} ♥ / {self.attaque} ⚔)"

    def __eq__(self, objet_comparaison: object) -> bool:
        # Si l'objet de comparaison n'est pas un personnage (ou un enfant)
        if not isinstance(objet_comparaison, Personnage):
            return False
        
        # Si les deux objets ont le même nom et la même vie
        if (self.nom == objet_comparaison.nom) and (self.vie == objet_comparaison.vie):
            return True
        
        return False