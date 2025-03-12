from abc import abstractmethod

from models.Alert import Alert
from models.Enums import MeasureType


class Mesure:
    """
    classe Mesure (abstraite) représente une valeur mesurée à un instant donné avec un type de mesure

    Attributs:
        type (MeasureType): type de mesure (température ambiante, heure de sortie, durée des sorties, durée d'inactivité)
        value (float): valeur mesurée
        timestamp: timestamp de la mesure
    """

    def __init__(self, type: MeasureType, value: float, timestamp):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    @property
    def type(self) -> MeasureType:
        return self._type

    @type.setter
    def type(self, type: MeasureType):
        self._type = type

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        if value < 0:
            raise ValueError("La valeur mesurée ne peut pas être négative")
        self._value = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @abstractmethod
    def validate_value(self) -> Alert:
        pass

    def __str__(self):
        return f"{self._type} : {self._value} à {self._timestamp}"
