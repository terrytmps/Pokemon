"""
Paralysis status_effects strategy class
"""

import copy
import random

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy

"""
Paralysis status_effects strategy class
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
