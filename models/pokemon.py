from models.enum.xp_difficulty import XPDifficulty
from models.Decorator.Component import Component
from typing import List
from models.Observer.LevelObserver import LevelObserver


class Pokemon(LevelObserver):
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

        self.name = name
        self._level = level
        self.max_hp = max_hp
        self._current_hp = max_hp
        self._sprite_url = sprite_url
        self._xp_difficulty = xp_difficulty
        self._current_xp = 0
        self._moves = [None] * 4
        self.price = price
        self._level_observers: List[LevelObserver] = []

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

    ## Observer pattern methods

    def add_level_observer(self, observer: LevelObserver) -> None:
        if observer not in self._level_observers:
            self._level_observers.append(observer)

    def remove_level_observer(self, observer: LevelObserver) -> None:
        if observer in self._level_observers:
            self._level_observers.remove(observer)

    def notify_level_up(self, old_level: int, new_level: int) -> None:
        for observer in self._level_observers:
            observer.on_level_up(self, old_level, new_level)

    """
    Handle all logic behind levelUp
    """

    def levelUp(self, value):
        self._current_xp += value * self._xp_difficulty.value
        old_level = self._level

        # Check if the pokemon has enough xp to level up
        levels_gained = 0
        while self._current_xp >= self._level:
            self._current_xp -= self._level
            self._level += 1
            levels_gained += 1

        # Check if the pokemon has leveled up
        if levels_gained > 0:
            self.notify_level_up(old_level, self._level)
