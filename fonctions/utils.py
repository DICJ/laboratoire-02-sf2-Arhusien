import os
from typing import Any

def convertir_valeur(
    valeur: str | int | float | bool,
    type_cible: type,
    valeur_par_defaut: Any | None = None
) -> Any:
    """
    Convertis une valeur en un type cible.

    Parameters:
        valeur (str | int | float | bool): La valeur à convertir.
        type_cible (type): Le type cible.
        valeur_par_defaut (Any, optional): La valeur par défaut si la conversion échoue. Par défaut None.

    Returns:
        (Any): La valeur convertie ou la valeur par défaut.
    """

    # Essayer de convertir
    try:
        # Convertir la valeur dans le type cible
        valeur = type_cible(valeur)
    # Intercepter l'erreur (s'il y a)
    except:
        # Si la valeur n'a pas pu être convertie, retourner la valeur par défaut
        return valeur_par_defaut

    # Sinon, retourner la valeur convertie
    return valeur

def est_dans_intervalle(
    valeur: int | float,
    min: int | float,
    max: int | float
) -> bool:
    """
    Vérifie si une valeur numérique est incluse dans un intervalle (inclusif) spécifique.

    Parameters:
        valeur (int | float): La valeur numérique à vérifier.
        min (int | float): La borne minimale de l'intervalle.
        max (int | float): La borne maximale de l'intervalle.

    Returns:
        (bool): Si la valeur est incluse ou non dans l'intevalle.
    """

    # Si la valeur est inférieure à la valeur minimale
    if valeur < min:
        return False

    # Si la valeur est supérieur à la valeur maximale
    if valeur > max:
        return False

    # Sinon, la valeur est incluse dans l'intervalle
    return True

def est_nombre_entier(nombre: str | int) -> bool:
    """
    Détermine si un nombre est entier.
    
    Parameters:
        nombre (str | int): Le nombre à vérifier.

    Returns:
        (bool): Si le nombre est entier ou non.
    """

    # Si le nombre est un string et que le string est vide
    if isinstance(nombre, str) and not nombre:
        return False

    # Si le nombre est déjà un entier
    if isinstance(nombre, int):
        return True

    # Essayer de convertir le nombre en integer
    try:
        int(nombre)
    # Si le nombre n'a pas pu être converti, il ne s'agit pas d'un nombre entier
    except:
        return False

    # Sinon, le nombre est un nombre entier
    return True

def nettoyer_terminal() -> None:
    """
    Supprime le contenu du terminal.
    """

    # Exécuter la commande
    # https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cls
    os.system("cls")
