import copy
import random

from models.level.Stats import Stat
from models.status.NormalStatusStrategy import NormalStatusStrategy
from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Sleep status strategy class effect: 
- Pokemon is asleep and cannot attack
- 50% chance to wake up at the end of the turn
"""


class SleepStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.SLEEP

    def stat_change(self, pokemon) -> Stat:
        # nothing happens
        return copy.copy(pokemon.stat)

    def attack(self) -> bool:
        return False

    def end_turn(self, pokemon) -> None:
        # 50% chance to wake up
        if random.random() < 0.5:
            pokemon.status_strategy = NormalStatusStrategy()
