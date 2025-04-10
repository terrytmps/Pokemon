import copy
import random

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.normal_status_strategy import NormalStatusStrategy
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy

"""
Sleep status_effects strategy class effect: 
- Pokemon is asleep and cannot attack
- 50% chance to wake up at the end of the turn
"""


class SleepStatusStrategy(StatusStrategy):

    first_turn = True

    def get_status(self) -> StatusEnum:
        return StatusEnum.SLEEP

    def stat_change(self, pokemon) -> Stat:
        # nothing happens
        return copy.copy(pokemon.stat)

    def attack(self) -> bool:
        return False

    def end_turn(self, pokemon) -> None:
        # 50% chance to wake up
        if self.first_turn:
            self.first_turn = False
            return
        if random.random() < 0.5:
            pokemon.status_strategy = NormalStatusStrategy()
