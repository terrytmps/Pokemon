from abc import ABC
from pokemon_app.core.level.Stats import LevelObserver
from typing import List

"""
Allow a observable to notify observer when important event happen to him like level up or death
"""


class LevelObservable(ABC):
    def __init__(self):
        self._level_observers: List[LevelObserver] = []

    def subscribe_level_observer(self, observer: LevelObserver) -> None:
        """
        Subscribe an observer to the level observable.
        """
        if observer not in self._level_observers:
            self._level_observers.append(observer)

    def unsubscribe_level_observer(self, observer: LevelObserver) -> None:
        """
        Unsubscribe an observer from the level observable.
        """
        if observer in self._level_observers:
            self._level_observers.remove(observer)

    def notify_level_up(self, old_level: int, new_level: int) -> None:
        """ "
        Notify all observers about a level up event."
        """
        for observer in self._level_observers:
            observer.on_level_up(self, old_level, new_level)

    def notify_dead(self) -> None:
        for observer in self._level_observers:
            observer.on_dead(self)
