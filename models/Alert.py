from models.Room import Room
from models.Enums.MeasureType import MeasureType
from datetime import datetime
from models.Enums.LevelAlert import LevelAlert


class Alert:
    """
    La classe Alert gère les alertes générées par le système de surveillance.

    Attributs:
        alert_type (MeasureType): type d'alerte (le même que le type de mesure)
        message (str): message associé à l'alerte
        timestamp (DateTime): timestamp de l'alerte
        isActive (bool): indique si l'alerte est active ou non
        niveau_gravite (str): niveau de gravité de l'alerte ("success", "warning", "danger")
        piece (Room): pièce associée à l'alerte
        valeur (float): valeur de l'alerte
    """

    def __init__(
        self,
        type_alerte: MeasureType,
        message: str,
        niveau_gravite: LevelAlert,
        piece=None,
        timestamp=datetime.now(),
        valeur=None,
    ):
        self.type_alerte = type_alerte
        self.message = message
        self.niveau_gravite = niveau_gravite
        self.timestamp = timestamp
        self.isActive = True
        self.piece = piece
        self.valeur = valeur

    @property
    def type_alerte(self):
        return self._type_alerte

    @type_alerte.setter
    def type_alerte(self, type_alerte):
        if not isinstance(type_alerte, MeasureType):
            raise ValueError("Le type d'alerte doit être une instance de Type")
        self._type_alerte = type_alerte

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        if not isinstance(message, str):
            raise ValueError("Le message doit être une chaîne de caractères")
        self._message = message

    @property
    def niveau_gravite(self):
        return self._niveau_gravite

    @niveau_gravite.setter
    def niveau_gravite(self, niveau_gravite):
        if not isinstance(niveau_gravite, LevelAlert):
            raise ValueError(
                "Le niveau de gravité doit être une instance de LevelAlert"
            )
        self._niveau_gravite = niveau_gravite

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        if piece is not None and not isinstance(piece, Room):
            raise ValueError("La pièce doit être une instance de Room ou None")
        self._piece = piece

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if not isinstance(timestamp, datetime):
            raise ValueError("Le timestamp doit être une instance de datetime")
        self._timestamp = timestamp

    def calculate_priority(self, evaluateur) -> str:
        priority = evaluateur.evaluer(self)
        self.priority = priority
        return str(priority)

    def to_tuple(self):
        return (self.niveau_gravite, self.message)

    def __str__(self):
        return f"{self._type_alerte} : {self._message} à {self.timestamp}"
