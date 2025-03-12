from datetime import datetime
from models.EvaluateurPriorite import EvaluateurPriorite
from models.Alert import Alert
from models.Enums.LevelAlert import LevelAlert
from models.Enums.MeasureType import MeasureType
from models.Enums.PriorityLevel import PriorityLevel
from models.Room import Room


def test_priority_classification():
    alert = Alert(
        niveau_gravite=LevelAlert.DANGER,
        type_alerte=MeasureType.TEMPERATURE,
        message="Mesure de la température",
    )
    evaluateur = EvaluateurPriorite()

    priority = evaluateur.evaluer(alert)

    assert (
        priority == PriorityLevel.URGENT
    ), "L'alerte de niveau DANGER devrait être classée comme URGENT."


def test_priority_time_context():
    room = Room("Salon", None, 20)
    alert_day = Alert(
        niveau_gravite=LevelAlert.WARNING,
        type_alerte=MeasureType.TEMPERATURE,
        message="Mesure de la température",
        timestamp=datetime(2025, 2, 12, 14, 0, 0),  # jour
        piece=room,
    )
    alert_night = Alert(
        niveau_gravite=LevelAlert.WARNING,
        type_alerte=MeasureType.TEMPERATURE,
        message="Mesure de la température",
        timestamp=datetime(2025, 2, 12, 23, 0, 0),  # nuit
        piece=room,
    )
    evaluateur = EvaluateurPriorite()

    priority_day = evaluateur.evaluer(alert_day)
    priority_night = evaluateur.evaluer(alert_night)

    assert (
        priority_night.value > priority_day.value
    ), "Une alerte TEMPERATURE la nuit doit être plus critique que la même alerte en journée."


def test_priority_alert_accumulation():
    room = Room("Salon", None, 20)
    alert1 = Alert(
        niveau_gravite=LevelAlert.WARNING,
        type_alerte=MeasureType.DUREE_INACTIVITE,
        message="Mesure de la durée d'inactivité",
        piece=room,
    )
    alert2 = Alert(
        niveau_gravite=LevelAlert.WARNING,
        type_alerte=MeasureType.HEURE_SORTIE,
        message="Mesure de l'heure de sortie",
        piece=room,
    )
    evaluateur = EvaluateurPriorite()

    priority1 = evaluateur.evaluer(alert1)
    priority2 = evaluateur.evaluer(alert2)

    assert (
        priority2.value > priority1.value
    ), "L'accumulation d'alertes dans la même pièce doit augmenter la priorité."
