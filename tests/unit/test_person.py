import datetime

import pytest

from models.Activity import Activity
from models.Enums.ActivityType import ActivityType
from models.Home import Home
from models.Person import Person
from models.Room import Room
from models.Surveillance import Surveillance


@pytest.fixture
def surveillance():
    return Surveillance()


@pytest.fixture
def home(surveillance):
    return Home(surveillance, "123 Rue de Python")


@pytest.fixture
def room(home):
    return Room("Salon", home, 10)


@pytest.fixture
def person(room, home):
    return Person("Alice", room, home)


class TestPerson:
    def test_initialisation(self, person, home, room):
        """Teste l'initialisation de la classe Person."""
        assert person.name == "Alice"
        assert person.home == home
        assert person.room == room
        assert person.events == []
        assert person.activity is None

    @pytest.mark.parametrize("invalid_name", [123, None, [], {}])
    def test_name_invalide(self, invalid_name, room, home):
        """Teste la validation du nom."""
        with pytest.raises(ValueError):
            Person(invalid_name, room, home)

    def test_get_current_room(self, person):
        """Teste la récupération de la pièce actuelle de la personne."""
        assert person.getCurrentRoom() == person.room

    def test_get_activities(self, person):
        """Teste la récupération de l'activité de la personne."""
        assert person.getActivities() is None

        activity = Activity(
            person, person.room, datetime.datetime.now(), 10, ActivityType.ACTIVITY
        )
        person.addActivity(activity)
        assert person.getActivities() == activity
