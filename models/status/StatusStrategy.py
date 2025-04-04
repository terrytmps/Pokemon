from abc import abstractmethod

from models.level.Stats import Stat
from models.status.StatusEnum import StatusEnum

"""
StatusStrategy is an interface for the Strategy pattern.
It allow status effect on pokemon to change dynamically and behavior to be modified.
"""


class StatusStrategy:
    """
    Get the status of the pokemon
    """

    @abstractmethod
    def get_status(self) -> StatusEnum:
        pass

    """
    Modify the stats of the pokemon while he has status effect 
    """

    @abstractmethod
    def stat_change(self, pokemon) -> Stat:
        pass

    """
    Modify the behavior of the pokemon while he attack
    """

    @abstractmethod
    def attack(self) -> bool:
        pass

    """
    Modify the behavior of the pokemon while it's his end of the turn
    """

    @abstractmethod
    def end_turn(self, pokemon) -> None:
        pass
