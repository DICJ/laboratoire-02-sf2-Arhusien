from classes.Personnage import Personnage
from classes.DetailsCombat import DetailsCombat

class Arene:
    """
    Représente une arène, permet sa gestion et d'y organiser des combats.
    """

    def __init__(self):
        self._lst_personnages: list[Personnage] = []

        self._lst_combats: list[DetailsCombat] = []

    @property
    def lst_personnages(self):
        return self._lst_personnages
    
    def ajouter_personnage(self, personnage: Personnage) -> list[Personnage]:
        """
        Ajoute un personnage à la liste des personnages de l'arène.

        Parameters:
            personnage (Personnage): Le personnage à ajouter.

        Returns:
            (list[Personnage]): La nouvelle liste des personnages de l'arène.
        """

        # Si l'argument n'est pas une instance de la classe Personnage ou une instance d'une classe enfant
        if not isinstance(personnage, Personnage):
            raise TypeError("« Personnage » doit être de type « Personnage » ou d'une instance de classe enfant à « Personnage ».")
        
        # Ajouter le personnage à la liste
        self._lst_personnages.append(personnage)

        return self._lst_personnages
    
    def afficher_personnages(self, avec_compte: bool | None = False) -> list[str]:
        """
        Affiche la description de chacun des personnages.

        Parameters:
            avec_compte (bool, optionel): Si le compte des personnages de l'arène doit être inclut.

        Returns:
            (list[str]): Une liste contenant la description de chacun des personnages.
        """

        # Définir une liste vide qui contiendra la description des personnages
        lst_txt_personnages: list[str] = []
        # Parcourir la liste des personnages de l'arène
        for personnage in self._lst_personnages:
            # Ajouter la description du personnage de l'itération à la liste
            lst_txt_personnages.append(str(personnage))

        if avec_compte:
            lst_txt_personnages.insert(0, f"L'arène compte [blue]{len(self)}[/blue] personnages.\n")
        
        return lst_txt_personnages
    
    def soigner_personnage(self, personnage: Personnage) -> Personnage:
        """
        Soigne un personnage.

        Parameters:
            personnage (Personnage): Le personnage à soigner.

        Returns:
            (Personnage): Le personnage soigné.
        
        """

        # Si l'argument n'est pas une instance de la classe Personnage ou une instance d'une classe enfant
        if not isinstance(personnage, Personnage):
            raise TypeError("« Personnage » doit être de type « Personnage » ou d'une instance de classe enfant à « Personnage ».")
        
        # Réinitialiser le personnage
        personnage.reinitialiser_vie()

        return personnage

    def organiser_combat(self, lst_combattants: list[Personnage, Personnage], avec_enregistrement: bool | None = True) -> list[str]:
        """
        Organise un combat entre deux personnages.

        Parameters:
            lst_combattants (list[Personnage, Personnage]): Une liste contenant l'attaquant et le défenseur (dans cet ordre).
            avec_enregistrement (bool, optionel): Si les détails du combat doivent être ajoutés à l'historique des combats

        Returns:
            (list[str]): Une liste contenant un résumé, tour par tour, du combat.
        """

        # Créer une instance de la classe DetailsCombat pour représenter les détails de ce combat
        details_combat = DetailsCombat(lst_combattants)
        
        # Définir les rôles initials
        perso_attaquant = lst_combattants[0]
        perso_defenseur = lst_combattants[1]
        
        # Si la liste des combattants ne contient pas strictement des instances de la classe Personnage ou d'instances d'une classe enfant
        if not (isinstance(perso_attaquant, Personnage) and isinstance(perso_defenseur, Personnage)):
            raise TypeError("« Lst_combattants » doit contenir des éléments de type « Personnage » ou d'une instance de classe enfant à « Personnage ».")

        # Définir une liste vide qui contiendra le résumé du combat
        lst_txt_resume: list[str] = []
        # Boucler tant que l'attaquant et le défenseur possède plus de 0 point de vie
        while (perso_attaquant.vie > 0) and (perso_defenseur.vie > 0):
            details_combat.incrementer_nb_tours()

            # Récupérer le nombre de dégâts infligés par l'attaquant
            degats_infliges = perso_attaquant.attaquer()
            # Faire subrir ce nombre de dégâts au défenseur
            perso_defenseur.subir_degats(degats_infliges)

            # Ajouter cette attaque à la liste du résumé
            lst_txt_resume.append(f"{perso_attaquant.nom} assène un coup à {perso_defenseur.nom}, il lui inflige [blue]{degats_infliges} dégâts[/blue] !")

            # Si le défenseur n'a plus de point de vie à la suite de l'attaque
            if perso_defenseur.vie <= 0:
                lst_txt_resume.extend([
                    f"[red]{perso_defenseur.nom} est tombé, après un {"court" if details_combat.nb_tours < 5 else "long"} combat.[/red]",
                    f"[green]{perso_attaquant.nom} est vainqueur ![/green]"
                ])
                # Définir le vainqueur du combat dans les détails du combat
                details_combat.vainqueur = perso_attaquant
                # Ajouter les détails de ce combat dans la liste de l'historique des combats
                if avec_enregistrement:
                    self._lst_combats.append(details_combat)
                # Arrêter la boucle
                break
        
            # Inter-changer les rôles, l'attaque devient défenseur et le défenseur l'attaquant
            perso_attaquant, perso_defenseur = perso_defenseur, perso_attaquant
            
        return lst_txt_resume
    
    def organiser_bataille_royale(self) -> list[str]:
        """
        Organise un combat en match à mort avec tous les personnages de l'arène.

        Returns:
            (list[str]): Une liste contenant un résumé, tour par tour, de la bataille royale.
        """

        # Soigner tous les personnages avant de commencer
        for personnage in self._lst_personnages:
            self.soigner_personnage(personnage)

        # Définir une liste vide qui contiendra le résumé de la bataille royale
        lst_txt_resume: list[str] = []

        # Créer une instance de la classe DetailsCombat pour représenter les détails de ce combat
        details_combat = DetailsCombat(self._lst_personnages)

        # Boucler tant que la liste de personnages contient un personnage
        while len(self._lst_personnages) > 1:            
            # Faire combattre les deux premiers personnages de la liste
            lst_combattants = [self._lst_personnages[0], self._lst_personnages[1]]
            # Faire combattre les deux premiers personnages de la liste
            combat = self.organiser_combat(lst_combattants, avec_enregistrement=False)
            # Ajouter le résumé du combat à la liste
            lst_txt_resume.extend(combat)

            # Incrémenter le nombre de tours de la bataille royale
            details_combat.incrementer_nb_tours(len(combat) - 2)

            # Nettoyer l'arène
            self.nettoyer_arene()

            # Soigner le personnage survivant entre les combats
            if len(self._lst_personnages) > 0:
                self.soigner_personnage(self._lst_personnages[0])

        # Si la liste de personnage ne contient qu'un personnage
        if len(self._lst_personnages) == 1:
            lst_txt_resume.append(f"[yellow]{self._lst_personnages[0].nom} est vainqueur de la bataille royale ![/yellow]")
            # Définir le vainqueur du combat dans les détails du combat
            details_combat.vainqueur = self._lst_personnages[0]
            # Ajouter les détails de ce combat dans la liste de l'historique des combats
            self._lst_combats.append(details_combat)

        return lst_txt_resume

    def afficher_combats(self) -> list[str]:
        """
        Affiche l'historique des combats de l'arène.

        Returns:
            (list[str]): Une liste contenant l'historique de chacun des combats.
        """

        # Définir une liste vide qui contiendra l'historique des combats
        lst_txt_combats: list[str] = []
        # Parcourir la liste des combats de l'arène
        for combat in self._lst_combats:
            # Ajouter les détails du combat de l'itération à la liste
            lst_txt_combats.append(str(combat))

        return lst_txt_combats
    
    def nettoyer_arene(self) -> list[Personnage]:
        """
        Retire tous les personnages ayant 0 ou moins de vie de la liste des personnages de l'arène.

        Returns:
            (list[Personnage]): La nouvelle liste de personnages de l'arène.
        """

        # Filtrer la liste de personnages pour ne laisser que les personnages ayant encore des points de vie
        self._lst_personnages = list(filter(lambda p: p.vie > 0, self._lst_personnages))

        return self._lst_personnages

    def __len__(self) -> int:
        # Créer une liste filtrée ne contenant que les personnages ayant encore des points de vie
        lst_combattants = list(filter(lambda p: p.vie > 0, self._lst_personnages))

        # Retourner l longueur de cette liste
        return len(lst_combattants)
