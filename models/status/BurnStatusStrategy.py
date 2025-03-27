from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Represent burn status effect
Take 6% health damage every turn and reduce attack stat by 1/3
"""


class BurnStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.BURN

    def stat_change(self):
        # reduce attack stat by 1/3
        self._pokemon.attack_multiplier = 2/3

    def end_turn(self) -> None:
        # take 6% health damage
        pass

    def attack(self) -> None:
        # nothing
        pass
