from models.Alert import Alert
from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure
from models.Enums.LevelAlert import LevelAlert


class MesureHeureSortie(Mesure):
    """
    Mesure pour la duree de sortie
    Même attributs que mesure avec seulement le type déjà rempli
    """

    """
    Attributs statiques
    """
    horaire_sortie_tard = 22

    def __init__(self, value: float, timestamp):
        super().__init__(MeasureType.HEURE_SORTIE, value, timestamp)

    def validate_value(self) -> Alert:
        if self.value > MesureHeureSortie.horaire_sortie_tard:
            return Alert(
                MeasureType.HEURE_SORTIE, "Alerte : Sortie tardive!", LevelAlert.DANGER
            )
        return Alert(
            MeasureType.HEURE_SORTIE, "Heure de sortie correcte", LevelAlert.SUCCESS
        )
