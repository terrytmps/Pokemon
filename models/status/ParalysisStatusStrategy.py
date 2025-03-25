"""
Paralysis status strategy class
"""

from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Paralysis status strategy class
Speed is halved and the pokemon has a 25% chance of not being able to attack
"""


class ParalysisStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.PARALYSIS

    def stat_change(self):
        # reduce speed by half
        pass

    def attack(self) -> None:
        # 25% chance of not being able to attack
        pass

    def end_turn(self) -> None:
        # nothing
        pass
