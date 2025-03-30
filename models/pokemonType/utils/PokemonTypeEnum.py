from enum import Enum


class PokemonType(Enum):
    """
    Represent all implemented types in Pokémon with their corresponding image URL and color.
    """

    NONE = ("", "#A8A77A")  # Default (Normal)
    NORMAL = (
        "/static/img/logo-type/1.png",
        "#A8A77A",
    )
    FIGHT = (
        "/static/img/logo-type/2.png",
        "#C22E28",
    )
    FLYING = (
        "/static/img/logo-type/3.png",
        "#A98FF3",
    )
    POISON = (
        "/static/img/logo-type/4.png",
        "#A33EA1",
    )
    GROUND = (
        "/static/img/logo-type/5.png",
        "#E2BF65",
    )
    ROCK = (
        "/static/img/logo-type/6.png",
        "#B6A136",
    )
    BUG = (
        "/static/img/logo-type/7.png",
        "#A6B91A",
    )
    GHOST = (
        "/static/img/logo-type/8.png",
        "#735797",
    )
    STEEL = (
        "/static/img/logo-type/9.png",
        "#B7B7CE",
    )
    FIRE = (
        "/static/img/logo-type/10.png",
        "#EE8130",
    )
    WATER = (
        "/static/img/logo-type/11.png",
        "#6390F0",
    )
    GRASS = (
        "/static/img/logo-type/12.png",
        "#7AC74C",
    )
    ELECTRIC = (
        "/static/img/logo-type/13.png",
        "#F7D02C",
    )
    PSYCHIC = (
        "/static/img/logo-type/14.png",
        "#F95587",
    )
    ICE = (
        "/static/img/logo-type/15.png",
        "#96D9D6",
    )
    DRAGON = (
        "/static/img/logo-type/16.png",
        "#6F35FC",
    )
    DARK = (
        "/static/img/logo-type/17.png",
        "#705746",
    )

    def __init__(self, url, color):
        self._value_ = url  # Définit la valeur de l'Enum comme l'URL de l'image
        self.color = color  # Définit une couleur associée au type
