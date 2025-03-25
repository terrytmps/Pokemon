from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy

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

    def stat_change(self):
        # nothing happens
        pass

    def attack(self) -> None:
        # nothing happen
        pass

    def end_turn(self) -> None:
        # take damage and then if the pokemon is still alive, double the damage for next turn
        pass