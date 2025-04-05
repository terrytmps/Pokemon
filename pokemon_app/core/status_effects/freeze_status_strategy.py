import copy
import random

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.normal_status_strategy import NormalStatusStrategy
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy

"""
Represent the status_effects of a Pokemon when it is frozen
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
            pokemon.status_strategy = NormalStatusStrategy()
