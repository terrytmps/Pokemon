from models.enum.pokemon_type import PokemonType
from models.enum.xp_difficulty import XPDifficulty


class Pokemon:
    """
    Classe that represent a pokemon with all its attributes and behavior
    """

    def __init__(
        self,
        name: str,
        level: int,
        max_hp: int,
        sprite_url: str,
        xp_difficulty: XPDifficulty,
        first_type: PokemonType,
        second_type: PokemonType,
        price: int,
    ):

        self.name = name
        self._level = level
        self.max_hp = max_hp
        self._current_hp = max_hp
        self._sprite_url = sprite_url
        self._xp_difficulty = xp_difficulty
        self._current_xp = 0
        self.first_type = first_type
        self.second_type = second_type
        self._moves = [None] * 4
        self.price = price

    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = value
        if self._current_hp < 0:
            self._current_hp = 0
        if self._current_hp > self.max_hp:
            self._current_hp = self.max_hp

    @property
    def sprite_url(self):
        return self._sprite_url

    @property
    def level(self):
        return self._level

    """
    Handle all logic behind levelUp
    """

    def levelUp(self, value):
        self._current_xp += value * self._xp_difficulty.value
        while self._current_xp >= self._level:
            self._current_xp -= self._level
            self._level += 1

    """
    Try to add a move return boolean meaning success of operation
    """

    def addMove(self, move) -> bool:
        for i in range(4):
            if self._moves[i] is None:
                self._moves[i] = move
                return True
        return False

    """
    Try to replace a move return boolean meaning success of operation
    """

    def replaceMove(self, move, index) -> bool:
        if index < 0 or index > 3:
            return False
        self._moves[index] = move
        return True
