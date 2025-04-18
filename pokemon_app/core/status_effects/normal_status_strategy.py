import copy

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy

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
