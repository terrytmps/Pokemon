class Room:
    """
    Room : Représente une pièce de la maison
        • Contient des Mesure (température, etc.)
        • Lieu où se déroulent les Activity

    Attributs:
        name (str): nom de la pièce
        measures (List[Mesure]): liste des mesures de la pièce
        currentTemperature (float): température actuelle de la pièce
        activities (List[Activity]): liste des activités de la pièce
        home (Home): maison dans laquelle se trouve la pièce
    """

    def __init__(self, name: str, home, temperature: float):
        self.name = name
        self.home = home
        self.temperature = temperature
        if home is not None:
            home.addRoom(self)
        self.measures = []
        self.activities = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Le nom doit être une chaîne de caractères")
        self._name = name

    def addMeasure(self, measure):
        self.measures.append(measure)

    def addActivity(self, activity):
        self.activities.append(activity)

    def getMeasures(self):
        return self.measures

    def getActivities(self):
        return self.activities
