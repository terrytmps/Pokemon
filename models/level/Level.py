from models.level.LevelObservable import LevelObservable
from models.level.XpDifficulty import XPDifficulty

"""
Handle logic behing levelUp
"""


class Level(LevelObservable):
    def __init__(self, level: int, xp_difficulty: XPDifficulty):
        super().__init__()
        self._level: int = level
        self.__xp_difficulty: XPDifficulty = xp_difficulty
        self.__current_xp: int = 0

    def gain_experience(self, value):
        if self._level >= 100:
            return
        self.__current_xp += value * self.__xp_difficulty.value
        old_level = self._level

        # Check if the pokemon has enough xp to level up
        while self.__current_xp >= self._level:
            if self._level >= 100:
                return
            self.__current_xp -= self._level
            self._level += 1
            self.notify_level_up(old_level, self._level)

    def level_up_to(self, level: int):
        while self._level < level:
            self._level += 1
            self.notify_level_up(self._level - 1, self._level)

    @property
    def level(self):
        return self._level
