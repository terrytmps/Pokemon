import copy

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy

"""
Status poison effect

"""


class PoisonStatusStrategy(StatusStrategy):
    """
    6% health damage beginning
    """

    _damage = 6

    """
    40% max health damage
    """
    _max_damage = 48

    def get_status(self) -> StatusEnum:
        return StatusEnum.POISON

    def stat_change(self, pokemon) -> Stat:
        # nothing happens
        return copy.copy(pokemon.stat)

    def attack(self) -> bool:
        # nothing happen
        return True

    def end_turn(self, pokemon) -> None:
        # take damage and then if the pokemon is still alive, double the damage for next turn
        damage_percent = self._damage * pokemon.stat.current_max_hp // 100
        pokemon.take_damage(damage_percent)
        self._damage = max(self._damage * 2, self._max_damage)
