from models.Alert import Alert
from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure
from models.Enums.LevelAlert import LevelAlert


class MesureDureeSortie(Mesure):
    """
    Mesure pour la duree de sortie
    Même attributs que mesure avec seulement le type déjà rempli
    """

    """
    Attributs statiques
    """
    duree_sortie_prolongee = 8

    def __init__(self, value: float, timestamp):
        super().__init__(MeasureType.DUREE_SORTIE, value, timestamp)

    def validate_value(self) -> Alert:
        if self.value > MesureDureeSortie.duree_sortie_prolongee:
            return Alert(
                MeasureType.DUREE_SORTIE,
                "Alerte : Sortie prolongée!",
                LevelAlert.DANGER,
            )
        return Alert(
            MeasureType.DUREE_SORTIE, "Durée de sortie correcte", LevelAlert.SUCCESS
        )
