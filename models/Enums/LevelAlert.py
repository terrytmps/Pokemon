from enum import Enum


class LevelAlert(Enum):
    """
    LevelAlert : Représente un niveau d'alerte
    """

    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"

    def __str__(self):
        return self.value
