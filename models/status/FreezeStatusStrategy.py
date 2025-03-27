import copy
import random

from models.level.Stats import Stat
from models.status.NormalStatusStrategy import NormalStatusStrategy
from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Represent the status of a Pokemon when it is frozen
When attack is called, the Pokemon does nothing 
20% chance to defrost at the end of the turn
"""


class FreezeStatusStrategy(StatusStrategy):

    def get_status(self) -> StatusEnum:
        return StatusEnum.FREEZE

    def attack(self) -> bool:
        return False

    def stat_change(self, pokemon) -> Stat:
        return copy.copy(pokemon.stat)

    def end_turn(self, pokemon) -> None:
        # 20% chance to defrost and go back to normal
        if random.random() < 0.2:
            pokemon.status = NormalStatusStrategy()
