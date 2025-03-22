from abc import ABC, abstractmethod
from models.Observer.LevelObserver import LevelObserver


class LevelObservable(ABC):
    @abstractmethod
    def add_level_observer(self, observer: LevelObserver) -> None:
        pass

    @abstractmethod
    def remove_level_observer(self, observer: LevelObserver) -> None:
        pass

    @abstractmethod
    def notify_level_up(self, old_level: int, new_level: int) -> None:
        pass
