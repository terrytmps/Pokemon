from models.enum.xp_difficulty import XPDifficulty
from models.Observer.LevelObservable import LevelObservable


class Pokemon(LevelObservable):
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
        price: int,
    ):
        super().__init__()
        self.name = name
        self._level = level
        self.max_hp = max_hp
        self._current_hp = max_hp
        self._sprite_url = sprite_url
        self._xp_difficulty = xp_difficulty
        self._current_xp = 0
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

    @property
    def first_type(self):
        return None

    @property
    def second_type(self):
        return None

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

    ## Decorator pattern methods

    def get_types(self):
        """
        Return the types of the pokemon
        """
        return []

    def get_resistances(self):
        """ "
        Return the resistances of the pokemon
        """
        return []

    def get_weaknesses(self):
        """
        Return the weaknesses of the pokemon
        """
        return []

    def get_immunity(self):
        """
        Return the immunities of the pokemon
        """
        return []

    """
    Handle all logic behind levelUp
    """

    def levelUp(self, value):
        self._current_xp += value * self._xp_difficulty.value
        old_level = self._level

        # Check if the pokemon has enough xp to level up
        while self._current_xp >= self._level:
            self._current_xp -= self._level
            self._level += 1
            self.notify_level_up(old_level, self._level)
