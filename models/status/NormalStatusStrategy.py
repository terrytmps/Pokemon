from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Concrete Strategy class for Normal Status
Nothing it's the normal behavior
"""


class NormalStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        return StatusEnum.NORMAL

    def stat_change(self):
        pass

    def attack(self) -> None:
        pass

    def end_turn(self) -> None:
        pass
