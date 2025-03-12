class Home:
    """
    Home : Classe principale qui représente la maison surveillée
        • Contient plusieurs Room
        • Associée à un système de Surveillance
        • Peut avoir plusieurs Person

    Attributs:
        rooms (List[Room]): liste des pièces de la maison
        address (str): adresse de la maison
        surveillance (Surveillance): instance de Surveillance
        persons (List[Person]): liste des personnes
    """

    def __init__(self, surveillance, address):
        self.rooms = []
        self._address = address
        self.surveillance = surveillance
        self.persons = []

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise ValueError("L'adresse doit être une chaîne de caractères")
        self._address = address

    def addRoom(self, room):
        self.rooms.append(room)

    def add_person(self, person):
        self.persons.append(person)

    def getPersons(self):
        return self.persons
