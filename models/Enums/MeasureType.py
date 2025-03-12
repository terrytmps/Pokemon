from enum import Enum


class MeasureType(Enum):
    """
    Enumération des types de mesures
    """

    TEMPERATURE = "temperature"
    HEURE_SORTIE = "heure_sortie"
    DUREE_SORTIE = "duree_sortie"
    DUREE_INACTIVITE = "duree_inactivite"

    def __str__(self):
        return self.value
