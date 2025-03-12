import pytest
from datetime import datetime
from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure


@pytest.fixture
def timestamp():
    """Fixture fournissant un timestamp (datetime) pour les tests."""
    return datetime.now()


@pytest.fixture
def mesure_temperature(timestamp):
    """Fixture fournissant une mesure de type TEMPERATURE avec une valeur valide."""
    return Mesure(MeasureType.TEMPERATURE, 20, timestamp)


@pytest.fixture
def mesure_heure_sortie(timestamp):
    """Fixture fournissant une mesure de type HEURE_SORTIE avec une valeur valide."""
    return Mesure(MeasureType.HEURE_SORTIE, 10, timestamp)


@pytest.fixture
def mesure_duree_sortie(timestamp):
    """Fixture fournissant une mesure de type DUREE_SORTIE avec une valeur valide."""
    return Mesure(MeasureType.DUREE_SORTIE, 30, timestamp)


@pytest.fixture
def mesure_duree_inactivite(timestamp):
    """Fixture fournissant une mesure de type DUREE_INACTIVITE avec une valeur valide."""
    return Mesure(MeasureType.DUREE_INACTIVITE, 0, timestamp)


class TestMesure:
    """Classe de tests pour la classe Mesure."""

    def test_creation_temperature_valid(self, timestamp):
        """Teste la création d'une mesure de température avec des valeurs valides."""
        mesure = Mesure(MeasureType.TEMPERATURE, 20, timestamp)
        assert mesure.type == MeasureType.TEMPERATURE
        assert mesure.value == 20
        assert mesure.timestamp == timestamp

    def test_creation_heure_sortie_valid(self, timestamp):
        """Teste la création d'une mesure d'heure de sortie avec des valeurs valides."""
        mesure = Mesure(MeasureType.HEURE_SORTIE, 25, timestamp)
        assert mesure.type == MeasureType.HEURE_SORTIE
        assert mesure.value == 25
        assert mesure.timestamp == timestamp

    def test_creation_duree_sortie_valid(self, timestamp):
        """Teste la création d'une mesure de durée de sortie avec des valeurs valides."""
        mesure = Mesure(MeasureType.DUREE_SORTIE, 12, timestamp)
        assert mesure.type == MeasureType.DUREE_SORTIE
        assert mesure.value == 12
        assert mesure.timestamp == timestamp

    def test_creation_duree_inactivite_valid(self, timestamp):
        """Teste la création d'une mesure de durée d'inactivité avec des valeurs valides."""
        mesure = Mesure(MeasureType.DUREE_INACTIVITE, 0, timestamp)
        assert mesure.type == MeasureType.DUREE_INACTIVITE
        assert mesure.value == 0
        assert mesure.timestamp == timestamp

    # Tests sur la validation de la valeur (la valeur ne peut être négative)

    @pytest.mark.parametrize("valeur", [-5, -0.1])
    def test_value_negative_creation(self, timestamp, valeur):
        """Teste la création d'une mesure avec une valeur négative (pour tout type) lève une ValueError."""
        with pytest.raises(ValueError):
            Mesure(MeasureType.TEMPERATURE, valeur, timestamp)

    def test_set_value_valid(self, mesure_temperature):
        """Teste la modification valide de la valeur."""
        mesure_temperature.value = 25
        assert mesure_temperature.value == 25

    @pytest.mark.parametrize("valeur", [-1, -10])
    def test_set_value_invalid(self, mesure_temperature, valeur):
        """Teste la modification invalide de la valeur (négative) qui doit lever une ValueError."""
        with pytest.raises(ValueError):
            mesure_temperature.value = valeur

    # Test de la gestion spécifique pour la durée d'inactivité : valeur négative interdite

    def test_duree_inactivite_negative(self, timestamp):
        """Teste qu'une mesure de durée d'inactivité négative lève une ValueError."""
        with pytest.raises(ValueError):
            Mesure(MeasureType.DUREE_INACTIVITE, -5, timestamp)
