"""
Paralysis status strategy class
"""

import copy
import random

from models.level.Stats import Stat
from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Paralysis status strategy class
Speed is halved and the pokemon has a 25% chance of not being able to attack
"""


class ParalysisStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.PARALYSIS

    def stat_change(self, pokemon) -> Stat:
        # reduce speed by half
        stat = copy.copy(pokemon.stat)
        stat.current_speed = stat.current_speed // 2
        return stat

    def attack(self) -> bool:
        # 25% chance of not being able to attack
        if random.random() < 0.25:
            return False
        else:
            return True

    def end_turn(self, pokemon) -> None:
        # nothing
        pass
