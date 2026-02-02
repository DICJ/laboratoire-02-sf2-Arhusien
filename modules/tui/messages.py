from rich.console import Console

console = Console()

def imprimer_succes(
    texte: str,
    sous_texte: str | None = None
) -> None:
    """
    Imprime un message de succès dans le terminal.

    Parameters:
        texte (str): Le texte à imprimer.
        sous_texte (str, optional): Le sous-texte à imprimer. Par défaut None.
    """
    
    texte = f"[green]•[/] {texte}"
    if sous_texte:
        texte += f"\n[bright_black]└─[/bright_black] [green]{sous_texte}[/]"
    
    # Imprimer le texte
    console.print(texte)

def imprimer_information(
    texte: str,
    sous_texte: str | None = None
) -> None:
    """
    Imprime un message d'information dans le terminal.
    
    Parameters:
        texte (str): Le texte à imprimer.
        sous_texte (str, optional): Le sous-texte à imprimer. Par défaut None.
    """
    
    texte = f"[blue]•[/] {texte}"
    if sous_texte:
        texte += f"\n[bright_black]└─[/bright_black] [blue]{sous_texte}[/]"
    
    # Imprimer le texte
    console.print(texte)

def imprimer_avertissement(
    texte: str,
    sous_texte: str | None = None
) -> None:
    """
    Imprime un message d'avertissement dans le terminal.
    
    Parameters:
        texte (str): Le texte à imprimer.
        sous_texte (str, optional): Le sous-texte à imprimer. Par défaut None.
    """

    texte = f"[yellow]•[/] {texte}"
    if sous_texte:
        texte += f"\n[bright_black]└─[/bright_black] [yellow]{sous_texte}[/]"
    
    # Imprimer le texte
    console.print(texte)

def imprimer_erreur(
    texte: str,
    sous_texte: str | None = None
) -> None:
    """
    Imprime un message d'erreur dans le terminal.
    
    Parameters:
        texte (str): Le texte à imprimer.
        sous_texte (str, optional): Le sous-texte à imprimer. Par défaut None.
    """

    texte = f"[red]•[/] {texte}"
    if sous_texte:
        texte += f"\n[bright_black]└─[/bright_black] [red]{sous_texte}[/]"
    
    # Imprimer le texte
    console.print(texte)
