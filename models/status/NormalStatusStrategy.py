import copy

from models.level.Stats import Stat
from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Concrete Strategy class for Normal Status
Nothing it's the normal behavior
"""


class NormalStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.NORMAL

    def stat_change(self, pokemon) -> Stat:
        return copy.copy(pokemon.stat)

    def attack(self) -> bool:
        return True

    def end_turn(self, pokemon) -> None:
        pass
