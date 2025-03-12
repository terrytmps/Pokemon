from models.Enums.ActivityType import ActivityType
from models.Person import Person
from models.Room import Room
from datetime import datetime


class Activity:
    """
    Activity : Représente les activités de la personne
        • Liée à une Person
        • Se déroule dans une Room
        • Peut générer des Alert

    Attributs:
        person (Person): personne effectuant l'activité
        room (Room): pièce dans laquelle se déroule l'activité
        timestamp: timestamp de l'activité
        duration (float) : durée de l'activité
        activity_type (ActivityType) : type d'activité
    """

    def __init__(
        self,
        person: Person,
        room: Room,
        timestamp: datetime,
        duration: float,
        activity_type: ActivityType,
    ):
        self.person = person
        self.room = room
        self.timestamp = timestamp
        self.duration = duration
        self.activity_type = activity_type
        person.addActivity(self)

    @property
    def person(self) -> Person:
        return self._person

    @person.setter
    def person(self, person: Person):
        if not isinstance(person, Person):
            raise ValueError("La personne doit être une instance de Person")
        self._person = person

    @property
    def room(self) -> Room:
        return self._room

    @room.setter
    def room(self, room: Room):
        if not isinstance(room, Room):
            raise ValueError("La pièce doit être une instance de Room")
        self._room = room

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        if not isinstance(timestamp, datetime):
            raise ValueError("Le timestamp doit être une instance de DateTime")
        self._timestamp = timestamp

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if duration < 0:
            raise ValueError("La durée ne peut pas être négative")
        self._duration = duration

    @property
    def activity_type(self) -> ActivityType:
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type: ActivityType):
        if not isinstance(activity_type, ActivityType):
            raise ValueError(
                "Le type d'activité doit être une instance de ActivityType"
            )
        self._activity_type = activity_type

    def __str__(self):
        return f"{self._activity_type} de {self._duration} à {self._timestamp}"
