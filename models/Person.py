from models.Home import Home
from models.Room import Room


class Person:
    """
    Person : Représente une personne surveillée
        • Effectue des Activity
        • Génère des Event
        • Peut être dans une Room

    Attributs:
        name (str): nom de la personne
        room (Room): pièce dans laquelle se trouve la personne
        home (Home): maison dans laquelle se trouve la personne
        activity (Activity): une Activity effetuée par la personne
        events (List[Event]): liste des événements générés par la personne
    """

    def __init__(self, name: str, room: Room, home: Home):
        self.name = name
        self.home = home
        home.add_person(self)
        self.room = room
        self.events = []
        self.activity = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Le nom doit être une chaîne de caractères")
        self._name = name

    def getCurrentRoom(self):
        return self.room

    def getActivities(self):
        return self.activity

    def addActivity(self, activity):
        self.activity = activity

    def addEvent(self, event):
        self.events.append(event)
