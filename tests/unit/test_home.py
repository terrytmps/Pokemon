import pytest
from models.Home import Home
from models.Surveillance import Surveillance
from models.Room import Room
from models.Person import Person


@pytest.fixture
def surveillance():
    return Surveillance()


@pytest.fixture
def home(surveillance):
    return Home(surveillance, "123 Rue de Python")


@pytest.fixture
def room(home):
    return Room("Salon", home, 10)  # Ensure we pass `home` as required


@pytest.fixture
def person(room, home):
    return Person("Alice", room, home)  # Ensure `room` and `home` are passed


class TestHome:
    def test_initialisation(self, home, surveillance):
        assert home.rooms == []
        assert home.address == "123 Rue de Python"
        assert home.surveillance == surveillance
        assert home.persons == []

    def test_room(self, home, room):
        assert len(home.rooms) == 1

    def test_add_room(self, home, room):
        home.addRoom(room)
        assert len(home.rooms) == 2
        assert home.rooms[1] == room

    def test_add_person(self, home, person):
        home.add_person(person)
        assert len(home.persons) == 2
        assert home.persons[1] == person

    def test_get_persons(self, home, person):
        person2 = Person("Bob", person.room, person.home)
        assert home.getPersons() == [person, person2]
