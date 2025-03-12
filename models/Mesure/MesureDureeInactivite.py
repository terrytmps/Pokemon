from models.Alert import Alert
from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure
from models.Enums.LevelAlert import LevelAlert


class MesureDureeInactivite(Mesure):
    """
    Mesure pour la duree inactivite
    Même attributs que mesure avec seulement le type déjà rempli
    """

    """
    Attributs statiques
    """
    duree_inactivite_prolongee = 2

    def __init__(self, value: float, timestamp):
        super().__init__(MeasureType.DUREE_INACTIVITE, value, timestamp)

    def validate_value(self) -> Alert:
        if self.value > MesureDureeInactivite.duree_inactivite_prolongee:
            return Alert(
                MeasureType.DUREE_INACTIVITE,
                "Alerte : Inactivité prolongée!",
                LevelAlert.DANGER,
            )
        return Alert(
            MeasureType.DUREE_INACTIVITE,
            "Durée d'inactivité correcte",
            LevelAlert.SUCCESS,
        )
