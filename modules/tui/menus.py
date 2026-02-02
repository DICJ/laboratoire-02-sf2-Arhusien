import os
from classes.Vehicule import Vehicule
from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from fonctions import course

# Créer une instance de la classe Console
console = Console()

# Essayer d'appeler la fonction
try:
    # Récupérer la longueur du terminal
    longueur_terminal = os.get_terminal_size().columns
# Intercepter l'erreur (s'il y a)
except:
    # Si la fonction n'a pas pu être appelée, définir une valeur par défaut
    longueur_terminal = 160

def creer_menu(
    titre: tuple[str, str] | str,
    lst_options: list[tuple[str, str] | str],
    sous_titre: str | None = None,
    nb_colonne: int | None = 1,
    commencer_a_zero: bool | None = False,
    mode_lecture: bool | None = False,
    longueur_max: bool | None = False
) -> Panel:
    """
    Construit un menu.

    Parameters:
        titre (tuple[str, str] | str): Le titre (et son style) du menu.
        lst_options (list[tuple[str, str] | str]): La liste des options (et leurs styles) du menu.
        sous_titre (str, optional): Le sous-titre du menu. Par défaut None.
        nb_colonne (int, optional): Le nombre de colonnes du menu. Par défaut 1.
        commencer_a_zero (bool, optional): Si les indices des options doivent commencer à 0. Par défaut False.
        mode_lexture (bool, optional): Si le menu n'est destiné qu'à être consulté, sans possibilité de choisir une option. Par défaut False.
        longueur_max (bool, optional): Si le menu doit être affiché sur toute la longueur du terminal. Par défaut False.

    Returns:
        (Panel): Un panneau Rich à imprimer dans le terminal.
    """

    style_titre = ""
    # Si le titre est un tuple
    if isinstance(titre, tuple):
        # Déconstruire le tuple et définir son contenu dans deux variables (texte et style)
        texte_titre, style_titre = titre
    # Si le titre est un string
    else:
        texte_titre = titre

    if longueur_max:
        longueur_totale = longueur_terminal
    else:
        # Transformer chaque option en liste contenant chacune des lignes de ladite option
        lst_lignes_options = [
            (option[0] if isinstance(option, tuple) else option).split('\n') for option in lst_options
        ]

        # Trouver la plus grande valeur parmi
        # la longueur du titre,
        # la longueur de la ligne d'option la plus longue
        # et la longueur du terminal divisée par 2
        longueur_totale = max(
            len(texte_titre),
            max(
                max(len(ligne) for ligne in option_lignes)
                for option_lignes in lst_lignes_options
            ),
            int(longueur_terminal / 2),
        )

    # Définir l'indice auquel commencera les positions des options dans la liste
    indice_de_depart = 0 if commencer_a_zero else 1

    # Définir le nombre d'options
    nb_options = len(lst_options)

    # Cérer une liste vide qui contiendra toutes les options formatées
    lst_options_texte = []
    # Parcourir la liste des options en associant à chaque option sa position dans la liste (tuple)
    for indice_option, option in enumerate(lst_options):
        style_option = ""
        # Si l'option est un tuple
        if isinstance(option, tuple):
            # Déconstruire le tuple et définir son contenu dans deux variables (texte et style)
            texte_option, style_option = option
        # Si l'option est un string
        else:
            texte_option = option

        # Définir le numéro de l'option
        indice_option_texte = "" if mode_lecture else f"[{indice_option + indice_de_depart}] "

        # Ajouter l'option dans la liste en la transformant en string et en lui ajoutant son style
        lst_options_texte.append(f"[{style_option}]{indice_option_texte}{texte_option}[/]" if style_option else f"{indice_option_texte}{texte_option}")

    # Créer une grille 
    # https://rich.readthedocs.io/en/latest/tables.html
    rendu_options = Table.grid(padding=(0, 10))
    # Ajouter des colonnes nb_colonne fois
    for i in range(nb_colonne):
        rendu_options.add_column(justify="left")

    # Boucler nb_options de fois en faisant des bons de nb_colonne et en débuant à 0
    for indice_debut_lot in range(0, nb_options, nb_colonne):
        # Récupérer l'indice de fin du lot d'options de la liste
        indice_fin_lot = indice_debut_lot + nb_colonne
        # Récupérer le lot d'options dans la liste
        lst_options_lot = lst_options_texte[indice_debut_lot:indice_fin_lot]

        # Désassembler la liste d'options du lot et l'intégrer à une rangée
        rendu_options.add_row(
            *lst_options_lot
        )

    # Créer un panneau
    # https://rich.readthedocs.io/en/latest/panel.html
    rendu_menu = Panel(
        renderable=rendu_options,
        box=box.HORIZONTALS,
        # Si le titre a un style, rendre le style et le titre, sinon, rendre titre
        title=f"[{style_titre}]{texte_titre}[/]" if style_titre else texte_titre,
        subtitle=f"[bright_black]{sous_titre}[/]" if sous_titre else None,
        subtitle_align="right",
        padding=(1, 1),
        border_style="bright_black",
        width=longueur_totale
    )

    # Retourner le panneau
    return rendu_menu

def imprimer_accueil() -> None:
    # Créer le menu
    menu = creer_menu(
        titre=("Accueil", "u white"),
        lst_options=[
            "Afficher les véhicules de votre garage",
            "Consulter la description d'un véhicule (et de ses composants)",
            "Calculer la vitesse maximale d'un véhicule",
            "Ajouter un ensemble de pneus à un véhicule",
            "Changer le moteur d'un véhicule",
            "Ajouter un véhicule à votre garage",
            "Faire concourir des véhicules",
            "Trouver le véhicule le plus rapide",
            "Compter le nombre de véhicules électriques",
            "Récupérer le nombre de véhicules fabriqués",
            ("Quitter", "red")
        ],
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_lst_vehicules(lst_vehicules: list[Vehicule], mode_lecture: bool | None = False) -> None:
    # Définir la liste des options du menu à partir de la liste des véhicules (ne garder que le nom de chaque véhicule)
    lst_options = [
        vehicule.nom for vehicule in lst_vehicules
    ]

    # Créer le menu
    menu = creer_menu(
        titre=("Liste des Véhicules", "u white"),
        lst_options=lst_options,
        mode_lecture=mode_lecture,
        sous_titre="R&D Automobile",
        commencer_a_zero=True
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_infos_vehicule(vehicule: Vehicule) -> None:
    # Récupérer la liste des informations du véhicule
    lst_infos = vehicule.obtenir_infos()
    # Si le véhicule est électrique
    if vehicule.est_electrique:
        lst_infos.append(("\nAttention ! Ce véhicule est électrique.", "yellow"))

    # Créer le menu
    menu = creer_menu(
        titre=(vehicule.nom.title(), "u white"),
        lst_options=lst_infos,
        mode_lecture=True,
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_vitesse(vehicule: Vehicule) -> None:
    # Récupérer la vitesse du véhicule
    vitesse_vehicule = vehicule.calculer_vitesse()
    # Transformer en km/h
    vitesse_vehicule = vitesse_vehicule * 3.6

    # Créer le menu
    menu = creer_menu(
        titre=(vehicule.nom.title(), "u white"),
        lst_options=[
            f"La vitesse maximale de ce véhicule est de [blue]{vitesse_vehicule} km/h[/blue]."
        ],
        mode_lecture=True,
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_resultat_simulation(dict_resultats: dict) -> None:
     # Cérer une liste vide qui contiendra tous les résultats formatés
    lst_resultats_txt = []
    # Parcourir le dictionnaire des résultats en associant à chaque résultat sa position(+1) dans la liste des valeurs du dictionnaire
    for position, resultat in enumerate(dict_resultats.values(), start=1):
        # Calculer le nombre d'espaces à placer devant chaque ligne d'informations du résultat
        espaces_a_placer = len(str(position)) + 2
        # Formater et ajouter le résultat à la liste
        lst_resultats_txt.append(
            f"[white]#{position} {resultat["nom"]}[/white]\n" +
            f"{" " * espaces_a_placer}[bright_black]├─[/bright_black] Temps : {course.formater_temps_course(resultat["temps"])} {f"([red]+{course.formater_temps_course(resultat["diff_temps"])}[/red])" if position > 1 else ""}\n" +
            f"{" " * espaces_a_placer}[bright_black]└─[/bright_black] Vitesse : {round((resultat["vitesse"] * 3.6), 2)} km/h"
        )

    # Créer le menu
    menu = creer_menu(
        titre=("Résultat de la Simulation", "u white"),
        lst_options=lst_resultats_txt,
        mode_lecture=True,
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_meilleur_vehicule(vehicule: Vehicule) -> None:
    # Créer le menu
    menu = creer_menu(
        titre=("Meilleur Véhicule", "u white"),
        lst_options=[
            f"Le véhicule le plus rapide de votre garage est [blue]{vehicule.nom}[/blue]."
        ],
        mode_lecture=True,
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_total_vehicules_electriques(nb_vehicules_electriques: int) -> None:
    # Créer le menu
    menu = creer_menu(
        titre=("Nombre de Véhicules Électriques", "u white"),
        lst_options=[
            f"Votre garage compte [blue]{nb_vehicules_electriques}[/blue] véhicules électriques."
        ],
        mode_lecture=True,
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)

def imprimer_total_vehicules_fabriques(nb_vehicules_fabriques: int) -> None:
    # Créer le menu
    menu = creer_menu(
        titre=("Nombre de Véhicules Électriques", "u white"),
        lst_options=[
            f"Le nombre de véhicules fabriqués est de [blue]{nb_vehicules_fabriques}[/blue] véhicules."
        ],
        mode_lecture=True,
        sous_titre="R&D Automobile"
    )

    # Imprimer le menu
    console.print(menu)
