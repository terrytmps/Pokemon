import pytest
from datetime import datetime

from models.Enums import MeasureType
from models.Event import Event
from models.Enums.EventType import EventType
from models.Home import Home
from models.Person import Person
from models.Situation import Situation
from models.Surveillance import Surveillance
from models.Alert import Alert


@pytest.fixture
def surveillance():
    return Surveillance()


@pytest.fixture
def home(surveillance):
    return Home(surveillance, "123 Rue de Python")


@pytest.fixture
def person(home):
    return Person("Alice", None, home)  # Assuming room and home are required


@pytest.fixture
def situation(surveillance):
    return Situation(datetime.now(), surveillance, None)


@pytest.fixture
def event(person, situation):
    return Event(
        person=person,
        timestamp=datetime.now(),
        situation=situation,
        eventType=EventType.TEMPERATURE,
        description="Test Event",
    )


class TestEvent:
    def test_event_initialization(self, event, person, situation):
        assert event.person == person
        assert isinstance(event.timestamp, datetime)
        assert event.situation == situation
        assert event.eventType == EventType.TEMPERATURE
        assert event.description == "Test Event"
        assert event.alert is None
