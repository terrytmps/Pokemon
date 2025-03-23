from models.level.LevelObservable import LevelObservable
from models.xp_difficulty import XPDifficulty

"""
Handle logic behing levelUp
"""
class Level(LevelObservable):
    def __init__(self, level: int, xp_difficulty: XPDifficulty):
        super().__init__()
        self._level = level
        self.__xp_difficulty = xp_difficulty
        self.__current_xp = 0

    def gain_experience(self, value):
        self.__current_xp += value * self.__xp_difficulty.value
        old_level = self._level

        # Check if the pokemon has enough xp to level up
        while self.__current_xp >= self._level:
            self.__current_xp -= self._level
            self._level += 1
            self.notify_level_up(old_level, self._level)

    @property
    def level(self):
        return self._level