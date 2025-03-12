import pytest
from datetime import datetime, timedelta

from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure
from service.MonitoringService import MonitoringService
from models.Enums.LevelAlert import LevelAlert


class DummyRequest:
    """Simule un objet request avec un attribut 'form'"""

    def __init__(self, form):
        self.form = form


class DummyAlert:
    """Simule l'objet retourné par surveillance.handleAlert()"""

    def __init__(self, message):
        self.message = message

    def to_tuple(self):
        return self.message


class DummySurveillance:
    """Simule l'objet de surveillance avec une méthode handleAlert qui renvoie une alerte sous forme de tuple"""

    def handleAlert(self, mesure: Mesure):
        return DummyAlert((mesure.type, mesure.value))


@pytest.fixture
def monitoring_service():
    return MonitoringService()


@pytest.fixture
def surveillance():
    """Crée une instance factice de surveillance"""
    return DummySurveillance()


@pytest.mark.parametrize(
    "form_data, expected_type, method",
    [
        ({"temperature": "25.5"}, MeasureType.TEMPERATURE, "temperature"),
        ({"heure_sortie": "8.0"}, MeasureType.HEURE_SORTIE, "sortie"),
        ({"duree_sortie": "3.5"}, MeasureType.DUREE_SORTIE, "duree_sortie"),
        (
            {"duree_inactivite": "4.2"},
            MeasureType.DUREE_INACTIVITE,
            "duree_inactivite",
        ),
    ],
)
def test_mesure_creation(monitoring_service, form_data, expected_type, method):
    """
    Teste la création d'une mesure pour chaque type via les méthodes internes
    """
    request = DummyRequest(form_data)
    if method == "temperature":
        mesure = monitoring_service._get_mesure_temperature(request)
    elif method == "sortie":
        mesure = monitoring_service._get_mesure_sortie(request)
    elif method == "duree_sortie":
        mesure = monitoring_service._get_mesure_duree_sortie(request)
    elif method == "duree_inactivite":
        mesure = monitoring_service._get_mesure_duree_inactivite(request)
    else:
        pytest.fail("Méthode non reconnue pour le test")

    assert mesure.type == expected_type
    expected_value = float(list(form_data.values())[0])
    assert mesure.value == expected_value

    now = datetime.now()
    assert (now - mesure.timestamp) < timedelta(seconds=10)


@pytest.mark.parametrize(
    "form_data",
    [
        {
            "temperature": "abc",
            "heure_sortie": "8.0",
            "duree_sortie": "3.5",
            "duree_inactivite": "4.2",
        },
        {
            "temperature": "25.5",
            "heure_sortie": "def",
            "duree_sortie": "3.5",
            "duree_inactivite": "4.2",
        },
        {
            "temperature": "25.5",
            "heure_sortie": "8.0",
            "duree_sortie": "ghi",
            "duree_inactivite": "4.2",
        },
        {
            "temperature": "25.5",
            "heure_sortie": "8.0",
            "duree_sortie": "3.5",
            "duree_inactivite": "jkl",
        },
    ],
)
def test_invalid_mesure_creation(monitoring_service, surveillance, form_data):
    """
    Teste que si une conversion en float échoue (entrée invalide)
    """
    request = DummyRequest(form_data)
    messages = monitoring_service.handle_form(request, surveillance)
    assert (
        LevelAlert.DANGER,
        "Erreur : Veuillez entrer des valeurs numériques valides",
    ) in messages


def test_alert_generation(monitoring_service, surveillance):
    """
    Teste la génération des alertes à partir d'une saisie valide
    """
    form_data = {
        "temperature": "25.5",
        "heure_sortie": "8.0",
        "duree_sortie": "3.5",
        "duree_inactivite": "4.2",
    }
    request = DummyRequest(form_data)
    messages = monitoring_service.handle_form(request, surveillance)

    expected = [
        (MeasureType.TEMPERATURE, 25.5),
        (MeasureType.HEURE_SORTIE, 8.0),
        (MeasureType.DUREE_SORTIE, 3.5),
        (MeasureType.DUREE_INACTIVITE, 4.2),
    ]
    assert messages == expected
