from enum import Enum


class EventType(Enum):
    """
    EventType : Représente un type d'événement
    """

    TEMPERATURE = "Température"
    OUT_LATE = "Sortie tardive"
    OUT_DURATION = "Sortie prolongée"
    INACTIVITY_DURATION = "Inactivité prolongée"

    def __str__(self):
        return self.value
