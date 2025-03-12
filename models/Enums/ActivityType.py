from enum import Enum


class ActivityType(Enum):
    """
    Enumération des types d'activités
    """

    INACTIVITY = "Inactivité"
    ACTIVITY = "Activité"

    def __str__(self):
        return self.value
