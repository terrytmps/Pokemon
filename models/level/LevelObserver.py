from abc import ABC, abstractmethod

""""
Observer that will handle and run logic when event happen to observable
"""


class LevelObserver(ABC):
    @abstractmethod
    def on_level_up(self, pokemon, old_level: int, new_level: int):
        pass

    @abstractmethod
    def on_dead(self, pokemon):
        pass