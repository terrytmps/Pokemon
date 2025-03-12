from enum import Enum


class PriorityLevel(Enum):
    """
    Enumération des niveaux de priorité
    """

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

    def __str__(self):
        return self.name
