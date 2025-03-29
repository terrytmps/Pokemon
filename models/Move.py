from models.enum.MoveCategory import MoveCategory
from models.pokemonType.utils.PokemonTypeEnum import PokemonType
from models.status.StatusEnum import StatusEnum


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
        move_effect: StatusEnum = StatusEnum.NORMAL
    ):
        self.name = name
        self.description = description
        self.power = power
        self.accuracy = accuracy
        self.move_type = move_type
        self.move_category = move_category
        self.move_effect = move_effect

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "power": self.power,
            "accuracy": self.accuracy,
            "move_type": self.move_type.name,
            "move_color": self.move_type.color,
            "move_category": self.move_category.name,
            "move_effect": self.move_effect.name
        }