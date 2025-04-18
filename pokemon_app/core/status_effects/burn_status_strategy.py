import copy

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy

"""
Represent burn status_effects effect
Take 6% health damage every turn and reduce attack stat by 1/3
"""


class BurnStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.BURN

    def stat_change(self, pokemon) -> Stat:
        # reduce attack by 1/3
        stat = copy.copy(pokemon.stat)
        stat.current_attack = stat.current_attack // 3
        return stat

    def end_turn(self, pokemon) -> None:
        # take 6% health damage
        damage_percent = 6 * pokemon.stat.current_max_hp // 100
        pokemon.take_damage(damage_percent)

    def attack(self) -> bool:
        # nothing
        return True
