from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Represent the status of a Pokemon when it is frozen
When attack is called, the Pokemon does nothing 
20% chance to defrost at the end of the turn
"""


class FreezeStatusStrategy(StatusStrategy):

    def get_status(self) -> StatusEnum:
        return StatusEnum.FREEZE

    def attack(self) -> None:
        return False

    def stat_change(self):
        # nothing happens
        pass

    def end_turn(self) -> None:
        # 20% chance to defrost and go back to normal
        pass
