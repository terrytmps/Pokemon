import pytest
from datetime import datetime
from models.Enums.ActivityType import ActivityType
from models.Person import Person
from models.Room import Room
from models.Activity import Activity
from models.Home import Home


@pytest.fixture
def home_valide():
    """Fixture fournissant une instance valide de Home."""
    return Home(surveillance=None, address="1223 Rue Saint Esprit, Sherbrooke")


@pytest.fixture
def personne_valide(home_valide, piece_valide):
    """Fixture fournissant une instance valide de Person."""
    return Person(name="Jean Dupont", room=piece_valide, home=home_valide)


@pytest.fixture
def piece_valide(home_valide):
    """Fixture fournissant une instance valide de Room."""
    return Room(name="Salon", home=home_valide, temperature=22.0)


@pytest.fixture
def activity_valide(personne_valide, piece_valide):
    """Fixture fournissant une instance valide d'Activity."""
    timestamp = datetime.now()
    return Activity(
        person=personne_valide,
        room=piece_valide,
        timestamp=timestamp,
        duration=30.0,
        activity_type=ActivityType.ACTIVITY,
    )


class TestActivity:
    """Classe de tests pour la classe Activity."""

    # Tests de création d'instances
    @pytest.mark.parametrize(
        "person_name, room_name, duration, activity_type",
        [
            ("Alice", "Cuisine", 45.0, ActivityType.ACTIVITY),
            ("Bob", "Chambre", 60.0, ActivityType.INACTIVITY),
        ],
    )
    def test_creation_valide(
        self, home_valide, person_name, room_name, duration, activity_type
    ):
        """Teste la création d'instances avec des valeurs valides."""
        room = Room(name=room_name, home=home_valide, temperature=22.0)
        person = Person(name=person_name, room=room, home=home_valide)
        timestamp = datetime.now()
        activity = Activity(
            person=person,
            room=room,
            timestamp=timestamp,
            duration=duration,
            activity_type=activity_type,
        )
        assert activity.person == person
        assert activity.room == room
        assert activity.timestamp == timestamp
        assert activity.duration == duration
        assert activity.activity_type == activity_type

    # Tests de validation des attributs
    @pytest.mark.parametrize("invalid_person", [None, "Not a Person", 123])
    def test_person_invalide(self, invalid_person, piece_valide):
        """Teste la création avec une personne invalide."""
        with pytest.raises(Exception):
            Activity(
                person=invalid_person,
                room=piece_valide,
                timestamp=datetime.now(),
                duration=30.0,
                activity_type=ActivityType.ACTIVITY,
            )

    @pytest.mark.parametrize("invalid_room", [None, "Not a Room", 123])
    def test_room_invalide(self, invalid_room, personne_valide):
        """Teste la création avec une pièce invalide."""
        with pytest.raises(ValueError, match="La pièce doit être une instance de Room"):
            Activity(
                person=personne_valide,
                room=invalid_room,
                timestamp=datetime.now(),
                duration=12,
                activity_type=ActivityType.ACTIVITY,
            )

    @pytest.mark.parametrize("invalid_timestamp", [None, "Not a DateTime", 123])
    def test_timestamp_invalide(self, invalid_timestamp, personne_valide, piece_valide):
        """Teste la création avec un timestamp invalide."""
        with pytest.raises(Exception):
            Activity(
                person=personne_valide,
                room=piece_valide,
                timestamp=invalid_timestamp,
                duration=12,
                activity_type=ActivityType.ACTIVITY,
            )

    @pytest.mark.parametrize("invalid_duration", [None, "Not a float", -10])
    def test_duration_invalide(self, invalid_duration, personne_valide, piece_valide):
        """Teste la création avec une durée invalide."""
        with pytest.raises(Exception):
            Activity(
                person=personne_valide,
                room=piece_valide,
                timestamp=datetime.now(),
                duration=invalid_duration,
                activity_type=ActivityType.INACTIVITY,
            )

    @pytest.mark.parametrize(
        "invalid_activity_type", [None, "Not an ActivityType", 123]
    )
    def test_activity_type_invalide(
        self, invalid_activity_type, personne_valide, piece_valide
    ):
        """Teste la création avec un type d'activité invalide."""
        with pytest.raises(
            ValueError,
            match="Le type d'activité doit être une instance de ActivityType",
        ):
            Activity(
                person=personne_valide,
                room=piece_valide,
                timestamp=datetime.now(),
                duration=30.0,
                activity_type=invalid_activity_type,
            )

    # Tests des setters
    def test_setter_person_invalide(self, activity_valide):
        """Teste la modification de la personne avec une valeur invalide."""
        with pytest.raises(Exception):
            activity_valide.person = "Not a Person"

    def test_setter_room_invalide(self, activity_valide):
        """Teste la modification de la pièce avec une valeur invalide."""
        with pytest.raises(ValueError, match="La pièce doit être une instance de Room"):
            activity_valide.room = "Not a Room"

    def test_setter_timestamp_invalide(self, activity_valide):
        """Teste la modification du timestamp avec une valeur invalide."""
        with pytest.raises(Exception):
            activity_valide.timestamp = "Not a DateTime"

    def test_setter_duration_invalide(self, activity_valide):
        """Teste la modification de la durée avec une valeur invalide."""
        with pytest.raises(Exception):
            activity_valide.duration = "Not a float"

    def test_setter_activity_type_invalide(self, activity_valide):
        """Teste la modification du type d'activité avec une valeur invalide."""
        with pytest.raises(
            ValueError,
            match="Le type d'activité doit être une instance de ActivityType",
        ):
            activity_valide.activity_type = "Not an ActivityType"
