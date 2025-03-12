import datetime

import pytest

from models.Enums.ActivityType import ActivityType
from models.Home import Home
from models.Person import Person
from models.Room import Room
from models.Mesure.Mesure import Mesure
from models.Activity import Activity
from models.Surveillance import Surveillance


@pytest.fixture
def surveillance():
    return Surveillance()


@pytest.fixture
def home(surveillance):
    return Home(surveillance, "123 Rue de Python")


@pytest.fixture
def room(home):
    return Room("Salon", home, 22.5)


@pytest.fixture
def person(room, home):
    return Person("Alice", room, home)


@pytest.fixture
def activity(room, person):
    return Activity(person, room, datetime.datetime.now(), 10, ActivityType.ACTIVITY)


class TestRoom:
    def test_initialisation(self, room, home):
        """Teste l'initialisation de la classe Room."""
        assert room.name == "Salon"
        assert room.home == home
        assert room.temperature == 22.5
        assert room.measures == []
        assert room.activities == []

    @pytest.mark.parametrize("invalid_name", [123, None, [], {}])
    def test_name_invalide(self, invalid_name, home):
        """Teste la validation du nom de la pièce."""
        with pytest.raises(ValueError):
            Room(invalid_name, home, 22.5)

    def test_add_measure(self, room):
        """Teste l'ajout d'une mesure."""
        mesure = Mesure("Température", 22.5, "ff")
        room.addMeasure(mesure)
        assert len(room.measures) == 1
        assert room.measures[0] == mesure

    def test_add_activity(self, room, activity):
        """Teste l'ajout d'une activité."""
        room.addActivity(activity)
        assert len(room.activities) == 1
        assert room.activities[0] == activity

    def test_get_measures(self, room):
        """Teste la récupération des mesures."""
        mesure = Mesure("Humidité", 45, "ff")
        room.addMeasure(mesure)
        assert room.getMeasures() == [mesure]

    def test_get_activities(self, room, activity):
        """Teste la récupération des activités."""

        room.addActivity(activity)
        assert room.getActivities() == [activity]
