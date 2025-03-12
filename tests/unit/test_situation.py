import pytest

from models.Enums import MeasureType
from models.Situation import Situation
from models.Surveillance import Surveillance
from models.Alert import Alert
from models.Mesure.Mesure import Mesure
from datetime import datetime
from models.Enums.LevelAlert import LevelAlert


@pytest.fixture
def surveillance():
    return Surveillance()


@pytest.fixture
def alerte():
    return Alert(
        MeasureType.MeasureType.TEMPERATURE,
        "Température trop basse!",
        LevelAlert.DANGER,
    )


@pytest.fixture
def situation(surveillance, alerte):
    return Situation(datetime.now(), surveillance, alerte)


@pytest.fixture
def mesure():
    return Mesure(MeasureType.MeasureType.TEMPERATURE, 22.5, datetime.now())


class TestSituation:
    def test_initialisation(self, situation, surveillance, alerte):
        """Teste l'initialisation de la classe Situation."""
        assert situation.timestamp is not None
        assert situation.surveillance == surveillance
        assert situation.alerte == alerte
        assert situation.mesures == []
        assert situation.events == []

    def test_add_mesure(self, situation, mesure):
        """Teste l'ajout d'une mesure."""
        situation.add_mesure(mesure)
        assert len(situation.mesures) == 1
        assert situation.mesures[0] == mesure

    def test_check_alert_conditions(self, situation, alerte, capsys):
        """Teste la vérification des conditions d'alerte."""
        alerte.isActive = True
        situation.checkAlertConditions()
        captured = capsys.readouterr()
        assert str(alerte) in captured.out
