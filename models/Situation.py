from models.Surveillance import Surveillance
from models.Alert import Alert
from models.Mesure.Mesure import Mesure
from datetime import datetime
from typing import List


class Situation:
    """
    Situation : Représente l'état global à un moment donné
        • Agrège plusieurs Mesure
        • Peut déclencher des Alert

    Attributs:
        timestamp (datetime): timestamp de la situation
        surveillance (Surveillance): instance de Surveillance
        mesures (List[Mesure]): liste des mesures
        alerte (Alerte): instance d'Alerte
        events (List['Event']): liste des événements
    """

    def __init__(self, timestamp: datetime, surveillance: Surveillance, alerte: Alert):
        self.timestamp = timestamp
        self.surveillance = surveillance
        self.mesures: List[Mesure] = []
        self.alerte = alerte
        self.events: List["Event"] = []

    def add_mesure(self, mesure: Mesure):
        self.mesures.append(mesure)

    def add_event(self, event: "Event"):
        self.events.append(event)

    def analyzeMeasures(self):
        pass

    def checkAlertConditions(self):
        if self.alerte.isActive:
            print(self.alerte)
