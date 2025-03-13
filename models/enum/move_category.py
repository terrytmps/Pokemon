from enum import Enum


class MoveCategory(Enum):
    """
    Represent the category of a move
    """
    STATUS = "status"
    PHYSICAL = "physical"
    SPECIAL = "special"
    OTHER = "other"