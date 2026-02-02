import os
from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

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
