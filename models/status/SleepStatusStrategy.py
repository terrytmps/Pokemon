from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

"""
Sleep status strategy class effect: 
- Pokemon is asleep and cannot attack
- 50% chance to wake up at the end of the turn
"""
class SleepStatusStrategy(StatusStrategy):
    def get_status(self) -> StatusEnum:
        # nothing happens
        pass

    def stat_change(self):
        # nothing happens
        pass

    def attack(self) -> None:
        # attack cancel because pokemon sleeping
        pass

    def end_turn(self) -> None:
        # 50% chance to wake up
        pass