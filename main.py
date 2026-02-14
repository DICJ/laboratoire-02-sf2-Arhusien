from classes.Archer import Archer
from classes.Mage import Mage
from classes.Guerrier import Guerrier
from classes.Soldat import Soldat
from classes.Berserker import Berserker
from classes.Arene import Arene
from modules.tui import menus, messages
from fonctions import utils

arene = Arene()

execution_en_cours = True
while execution_en_cours:
    menus.imprimer_accueil()
    choix_menu_accueil = input("Que souhaitez-vous faire ? ").strip()
   
    match choix_menu_accueil:
        # Si l'option sélectionné est « Ajouter un personnage à l'arène »
        case "1":
            type_personnage = input("Quel est le type du personnage (Guerrier, Mage, Archer, Soldat ou Berserker) ? ").strip()
            if (type_personnage.lower() not in ["guerrier", "mage", "archer", "soldat", "berserker"]):
                messages.imprimer_erreur("Ajout impossible", "Le type de personnage indiqué est invalide.")
                # Arrêter cette itération et passer à la suivante
                continue

            nom_personnage = input("Quel est le nom du personnage ? ").strip()
            vie_personnage = utils.convertir_valeur(input("Quel est le nombre de points de vie du personnage (de 0 à 500) ? ").strip(), int)
            attaque_personnage = utils.convertir_valeur(input("Quelle est la puissance d'attaque du personnage (de 0 à 50) ? ").strip(), int)

            personnage = None
            # Essayer de créer l'instance
            try:
                match type_personnage.lower():
                    case "guerrier":
                        force_personnage = utils.convertir_valeur(input("Quelle est la force du guerrier (de 1 à 50) ? ").strip(), int)

                        # Créer l'instance de la classe
                        personnage = Guerrier(nom_personnage, vie_personnage, attaque_personnage, force_personnage)
                    case "mage":
                        mana_personnage = utils.convertir_valeur(input("Quelle est la réserve de mana du mage (de 0 à 100) ? ").strip(), int)

                        # Créer l'instance de la classe
                        personnage = Mage(nom_personnage, vie_personnage, attaque_personnage, mana_personnage)
                    case "archer":
                        dexterite_personnage = utils.convertir_valeur(input("Quelle est la dextérité de l'archer (de 40 à 70) ? ").strip(), int)

                        # Créer l'instance de la classe
                        personnage = Archer(nom_personnage, vie_personnage, attaque_personnage, dexterite_personnage)
                    case "soldat":
                        # Créer l'instance de la classe
                        personnage = Soldat(nom_personnage, vie_personnage, attaque_personnage)
                    case "berserker":
                        force_personnage = utils.convertir_valeur(input("Quelle est la force du berserker (de 1 à 50) ? ").strip(), int)

                        # Créer l'instance de la classe
                        personnage = Berserker(nom_personnage, vie_personnage, attaque_personnage, force_personnage)
            # En cas d'erreur (retournée par un setter)
            except:
                messages.imprimer_erreur("Ajout impossible", "Les caractéristiques indiquées sont invalides.")
                # Arrêter cette itération et passer à la suivante
                continue

            # Ajouter le personnage à l'arène
            arene.ajouter_personnage(personnage)

            messages.imprimer_succes(f"{type_personnage.title()} ajouté à l'arène avec succès !")
        case "2" | "3" | "4":
            lst_personnages = arene.afficher_personnages(choix_menu_accueil == "2")

            # Si la liste de personnages est vide
            if len(lst_personnages) <= 0:
                messages.imprimer_erreur("Affichage impossible", "L'arène ne contient aucun personnage.")
                # Arrêter cette itération et passer à la suivante
                continue

            menus.imprimer_lst_personnages(lst_personnages, choix_menu_accueil == "2")
            
            match choix_menu_accueil:
                # Si l'option sélectionné est « Afficher les personnages de l'arène »
                case "2":
                    input("Quitter (Entrer) ")
                # Si l'option sélectionné est « Organiser un combat dans l'arène »
                case "3":
                    choix_indice_attaquant = utils.convertir_valeur(input("Quel personnage sera l'attaquant ? ").strip(), int, -1)
                    choix_indice_defenseur = utils.convertir_valeur(input("Quel personnage sera le défenseur ? ").strip(), int, -1)

                    # Si l'un des indices sélectionnés n'existe pas dans la liste
                    if not (
                        utils.est_dans_intervalle(choix_indice_attaquant, min=0, max=(len(arene.lst_personnages) - 1))
                        and utils.est_dans_intervalle(choix_indice_defenseur, min=0, max=(len(arene.lst_personnages) - 1))
                    ):
                        messages.imprimer_erreur("Sélection impossible", "L'un des personnages sélectionné n'existe pas.")
                        # Arrêter cette itération et passer à la suivante
                        continue

                    # Si les deux indices sont les mêmes
                    if choix_indice_attaquant == choix_indice_defenseur:
                        messages.imprimer_erreur("Sélection impossible", "Les deux combattants doivent être des personnages différents.")
                        # Arrêter cette itération et passer à la suivante
                        continue

                    input("Lancer (Entrer) ")

                    # Lancer le combat
                    resume_combat = arene.organiser_combat(lst_combattants=[
                        arene.lst_personnages[choix_indice_attaquant],
                        arene.lst_personnages[choix_indice_defenseur]
                    ])

                    menus.imprimer_resume_combat(resume_combat)

                    input("Quitter (Entrer) ")
                # Si l'option sélectionné est « Soigner un personnage de l'arène »
                case "4":
                    choix_indice_personnage = utils.convertir_valeur(input("Quel personnage souhaitez-vous soigner ? ").strip(), int, -1)

                    # Si l'indice sélectionné n'existe pas dans la liste
                    if not utils.est_dans_intervalle(choix_indice_personnage, min=0, max=(len(arene.lst_personnages) - 1)):
                        messages.imprimer_erreur("Sélection impossible", "Le personnage sélectionné n'existe pas.")
                        # Arrêter cette itération et passer à la suivante
                        continue

                    # Récupérer le personnage dans la liste des personnages de l'arène
                    personnage = arene.lst_personnages[choix_indice_personnage]
                    # Soigner le personnage
                    arene.soigner_personnage(personnage)

                    messages.imprimer_succes(f"{personnage.nom.title()} a été soigné avec succès !")
        # Si l'option sélectionné est « Nettoyer l'arène »
        case "5":
            arene.nettoyer_arene()

            messages.imprimer_succes(f"L'arène a été nettoyée avec succès !")
        # Si l'option sélectionné est « Organiser une bataille royale »
        case "6":
            # Lancer la bataille royale
            resume_combat = arene.organiser_bataille_royale()

            menus.imprimer_resume_combat(resume_combat)

            input("Quitter (Entrer) ")
        # Si l'option sélectionné est « Afficher tous les combats de l'arène »
        case "7":
            lst_combats = arene.afficher_combats()

            # Si la liste de combats est vide
            if len(lst_combats) <= 0:
                messages.imprimer_erreur("Affichage impossible", "L'arène n'a tenu aucun combat.")
                # Arrêter cette itération et passer à la suivante
                continue

            menus.imprimer_lst_combats(lst_combats)

            input("Quitter (Entrer) ")
        # Si l'option sélectionné est « Quitter »
        case "9":
            execution_en_cours = False
        case _:
            pass
