from enum import Enum


class MoveCategory(Enum):
    """
    Represent the category of a move
    """

    STATUS = "status_effects"
    PHYSICAL = "physical"
    SPECIAL = "special"
    OTHER = "other"
