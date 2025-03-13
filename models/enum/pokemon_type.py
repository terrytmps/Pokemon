from enum import Enum


class PokemonType(Enum):
    """
    Represent all implemented types in Pokémon with their corresponding image URL and color.
    """
    NONE = ("", "#A8A77A")  # Default (Normal)
    NORMAL = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/1.png", "#A8A77A")
    FIGHT = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/2.png", "#C22E28")
    FLYING = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/3.png", "#A98FF3")
    POISON = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/4.png", "#A33EA1")
    GROUND = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/5.png", "#E2BF65")
    ROCK = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/6.png", "#B6A136")
    BUG = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/7.png", "#A6B91A")
    GHOST = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/8.png", "#735797")
    STEEL = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/9.png", "#B7B7CE")
    FIRE = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/10.png", "#EE8130")
    WATER = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/11.png", "#6390F0")
    GRASS = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/12.png", "#7AC74C")
    ELECTRIC = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/13.png", "#F7D02C")
    PSYCHIC = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/14.png", "#F95587")
    ICE = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/15.png", "#96D9D6")
    DRAGON = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/16.png", "#6F35FC")
    DARK = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/17.png", "#705746")

    def __init__(self, url, color):
        self._value_ = url  # Définit la valeur de l'Enum comme l'URL de l'image
        self.color = color  # Définit une couleur associée au type
