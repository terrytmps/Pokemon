from abc import abstractmethod

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.status_enum import StatusEnum

"""
StatusStrategy is an interface for the Strategy pattern.
It allow status_effects effect on pokemon to change dynamically and behavior to be modified.
"""


class StatusStrategy:
    """
    Get the status_effects of the pokemon
    """

    @abstractmethod
    def get_status(self) -> StatusEnum:
        pass

    """
    Modify the stats of the pokemon while he has status_effects effect 
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
