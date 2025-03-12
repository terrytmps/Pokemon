from models.Enums.LevelAlert import LevelAlert
from models.Enums.PriorityLevel import PriorityLevel
from models.Alert import Alert
from models.Enums.MeasureType import MeasureType


class EvaluateurPriorite:
    """
    Classe responsable d'évaluer la priorité d'une alerte en fonction de différents critères.
    """

    def __init__(self):
        self.alert_counts = {}

    def evaluer(self, alerte: Alert) -> PriorityLevel:
        if alerte.niveau_gravite == LevelAlert.DANGER:
            base_value = PriorityLevel.URGENT.value
        elif alerte.niveau_gravite == LevelAlert.WARNING:
            base_value = PriorityLevel.HIGH.value
        elif alerte.niveau_gravite == LevelAlert.SUCCESS:
            base_value = PriorityLevel.LOW.value
        else:
            base_value = PriorityLevel.MEDIUM.value

        # Si l'alerte est de type température et qu'elle est reçue entre 20h et 6h, on augmente la priorité.
        alert_hour = alerte.timestamp.hour
        if alerte.type_alerte == MeasureType.TEMPERATURE and (
            alert_hour >= 20 or alert_hour < 6
        ):
            base_value = min(base_value + 1, PriorityLevel.URGENT.value)

        # Si l'alerte est associée à une pièce, on augmente la priorité en fonction du nombre d'alertes déjà reçues pour cette pièce.
        if alerte.piece is not None:
            room_key = id(alerte.piece)
            count = self.alert_counts.get(room_key, 0)
            base_value = min(base_value + count, PriorityLevel.URGENT.value)
            self.alert_counts[room_key] = count + 1

        # On retourne la priorité correspondante.
        for priority in PriorityLevel:
            if priority.value == base_value:
                return priority

        return PriorityLevel.MEDIUM  # Cas par défaut
