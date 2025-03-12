import pytest
from models.Alert import Alert
from models.Enums.MeasureType import MeasureType
from models.Enums.LevelAlert import LevelAlert


@pytest.fixture
def alerte_valide():
    """Fixture fournissant une instance valide d'Alert."""
    return Alert(MeasureType.TEMPERATURE, "Température normale", LevelAlert.SUCCESS)


class TestAlert:
    """Classe de tests pour la classe Alert."""

    # Tests de création d'instances
    @pytest.mark.parametrize(
        "type_alerte, message, niveau",
        [
            (MeasureType.HEURE_SORTIE, "Alerte : Sortie tardive!", LevelAlert.DANGER),
            (
                MeasureType.DUREE_INACTIVITE,
                "Alerte : Inactivité prolongée!",
                LevelAlert.DANGER,
            ),
            (MeasureType.TEMPERATURE, "Température normale", LevelAlert.SUCCESS),
        ],
    )
    def test_creation_valide(self, type_alerte, message, niveau):
        """Teste la création d'instances avec des valeurs valides."""
        alerte = Alert(type_alerte, message, niveau)
        assert alerte.type_alerte == type_alerte
        assert alerte.message == message
        assert alerte.niveau_gravite == niveau

    # Tests de validation du type_alerte.
    @pytest.mark.parametrize("type_invalide", [123, ["Température"], None])
    def test_type_alerte_invalide(self, type_invalide):
        """Teste la création avec un type d'alerte invalide."""
        with pytest.raises(ValueError):
            Alert(type_invalide, "Message valide", LevelAlert.SUCCESS)

    # Tests de validation du message.
    @pytest.mark.parametrize("message_invalide", [456, {"key": "value"}, 12.34])
    def test_message_invalide(self, message_invalide):
        """Teste la création avec un message invalide."""
        with pytest.raises(ValueError):
            Alert(MeasureType.TEMPERATURE, message_invalide, LevelAlert.WARNING)

    # Tests de validation du niveau de gravité.
    @pytest.mark.parametrize("niveau_invalide", ["erreur", "critical", 123])
    def test_niveau_gravite_invalide(self, niveau_invalide):
        """Teste la création avec un niveau de gravité invalide."""
        with pytest.raises(ValueError):
            Alert(MeasureType.TEMPERATURE, "Message valide", niveau_invalide)

    # Tests des setters
    def test_setter_type_alerte_invalide(self, alerte_valide):
        """Teste la modification du type d'alerte avec une valeur invalide."""
        with pytest.raises(ValueError):
            alerte_valide.type_alerte = 12345

    def test_setter_message_invalide(self, alerte_valide):
        """Teste la modification du message avec une valeur invalide."""
        with pytest.raises(ValueError):
            alerte_valide.message = ["Message invalide"]

    def test_setter_niveau_gravite_valide(self, alerte_valide):
        """Teste la modification valide du niveau de gravité."""
        alerte_valide.niveau_gravite = LevelAlert.WARNING
        assert alerte_valide.niveau_gravite == LevelAlert.WARNING

    # Test de la méthode to_tuple()
    def test_to_tuple(self, alerte_valide):
        """Vérifie le format de sortie de la méthode to_tuple()."""
        assert alerte_valide.to_tuple() == (LevelAlert.SUCCESS, "Température normale")
        alerte_valide.niveau_gravite = LevelAlert.DANGER
        assert alerte_valide.to_tuple()[0] == LevelAlert.DANGER
