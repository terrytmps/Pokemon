from xmlrpc.client import DateTime

from models.Enums.EventType import EventType
from models.Person import Person
from models.Situation import Situation


class Event:
    """
    Event : Représente un événement ponctuel
        • Lié à une Person
        • Peut générer une Alert
        • Associé à une Situation

    Attributs:
        person (Person): personne liée à l'événement
        timestamp (DateTime): timestamp de l'événement
        situation (Situation): situation associée à l'événement
        alert (Alert): possible alerte générée par l'événement
        eventType (EventType) : type d'événement
        description (str) : description de l'événement
    """

    def __init__(
        self,
        person: Person,
        timestamp: DateTime,
        situation: Situation,
        eventType: EventType,
        description: str,
    ):
        self.person = person
        self.timestamp = timestamp
        self.situation = situation
        self.eventType = eventType
        self.description = description
        self.alert = None
        person.addEvent(self)
        situation.add_event(self)
