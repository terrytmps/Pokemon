from models.Alert import Alert
from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure
from models.Enums.LevelAlert import LevelAlert


class MesureTemperature(Mesure):
    """
    Mesure pour la duree inactivite
    Même attributs que mesure avec seulement le type déjà rempli
    """

    """
    Attributs statiques
    """
    seuil_temperature_inferieur = 10
    seuil_temperature_superieur = 25

    def __init__(self, value: float, timestamp):
        super().__init__(MeasureType.TEMPERATURE, value, timestamp)

    def validate_value(self) -> Alert:
        if self.value < MesureTemperature.seuil_temperature_inferieur:
            return Alert(
                MeasureType.TEMPERATURE, "Température trop basse!", LevelAlert.DANGER
            )
        elif self.value > MesureTemperature.seuil_temperature_superieur:
            return Alert(
                MeasureType.TEMPERATURE, "Température trop élevée!", LevelAlert.DANGER
            )
        return Alert(MeasureType.TEMPERATURE, "Température normale", LevelAlert.SUCCESS)
