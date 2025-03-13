from models.enum.pokemon_type import PokemonType
from models.enum.xp_difficulty import XPDifficulty


class Pokemon:
    """
    Classe that represent a pokemon with all its attributes and behavior
    """

    def __init__(self, name, level, max_hp, sprite_url, xp_difficulty: XPDifficulty,
                 first_type: PokemonType, second_type: PokemonType):

        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.sprite_url = sprite_url
        self.xp_difficulty = xp_difficulty
        self.first_type = first_type
        self.second_type = second_type

