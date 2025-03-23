from models.enum.MoveCategory import MoveCategory
from models.pokemonType.PokemonTypeEnum import PokemonType


class Move:
    """
    Represent a move (attack or defense) that a pokemon can use
    """

    """
    accuracy: int between 0-100
    """

    def __init__(
        self,
        name: str,
        description: str,
        power: int,
        accuracy: int,
        move_type: PokemonType,
        move_category: MoveCategory,
    ):
        self.name = name
        self.description = description
        self.power = power
        self.accuracy = accuracy
        self.move_type = move_type
        self.move_category = move_category
